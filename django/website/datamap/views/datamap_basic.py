from __future__ import division
from django.core.urlresolvers import reverse
from django.http import (
    Http404,
    HttpResponseForbidden,
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

from braces.views import LoginRequiredMixin
from extra_views import (
    InlineFormSet
)
from datamap.models import Datamap, Field
from datamap.forms import FieldForm
from package.models import Package

from .maps import (
    single_datamap_not_normalized,
    datamaps_normalized,
    datamaps_normalized_sorted,
)


class DatamapView(DetailView):
    model = Datamap

    def get_queryset(self):
        return Datamap.objects.all().prefetch_related('dataset',
                                                      'format',
                                                      'fields',
                                                      'fields__concept',
                                                      'fields__translations')

    def get_context_data(self, *args, **kwargs):
        context = super(DatamapView,
                        self).get_context_data(*args, **kwargs)
        context['package'] = self.object.dataset
        context['visual'] = single_datamap_not_normalized(self.object)
        return context


class DatamapListView(ListView):
    model = Datamap

    def get_queryset(self):
        queryset = (
            Datamap.objects
            .all()
            .prefetch_related('dataset', 'dataset__publisher', 'format',
                              'fields', 'fields__concept')
            .order_by('dataset__publisher__country')
        )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(DatamapListView,
                        self).get_context_data(*args, **kwargs)
        datamaps = self.get_queryset()
        context['all_normalized'] = datamaps_normalized(datamaps)
        context['all_normalized_sorted'] = datamaps_normalized_sorted(datamaps)
        return context


class FieldInline(InlineFormSet):
    model = Field
    form_class = FieldForm


class DatamapAddView(LoginRequiredMixin, CreateView):
    action = 'Add'
    model = Datamap

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() and not user.profile.can_edit_package:
            return HttpResponseForbidden("permission denied")
        else:
            return super(DatamapAddView,
                         self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        dataset_id = request.GET.get('dataset')
        if not dataset_id >= 0:
            raise Http404
        self.dataset = Package.objects.get(pk=dataset_id)
        return super(DatamapAddView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        dataset_id = request.POST.get('dataset')
        if not dataset_id >= 0:
            raise Http404
        self.dataset = Package.objects.get(pk=dataset_id)
        return super(DatamapAddView, self).post(request, *args, **kwargs)

    def get_form(self, form_class):
        form_kwargs = self.get_form_kwargs()
        form_kwargs['initial'] = {'dataset': self.dataset.id}
        return form_class(**form_kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(DatamapAddView, self).get_context_data(*args, **kwargs)

        package = self.dataset
        context['package'] = package
        return context

    def get_success_url(self):
        return reverse('package', kwargs={'slug': self.dataset.slug})


class DatamapEditView(LoginRequiredMixin, UpdateView):
    action = 'Edit'
    model = Datamap

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() and not user.profile.can_edit_datamap:
            return HttpResponseForbidden("permission denied")
        else:
            return super(DatamapEditView,
                         self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('datamap', kwargs={'pk': self.object.id})

    def get_context_data(self, *args, **kwargs):
        context = super(DatamapEditView,
                        self).get_context_data(*args, **kwargs)

        context['action'] = self.action
        context['package'] = self.object.dataset
        context['datamap'] = self.object

        return context
