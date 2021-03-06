from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Link
from .serializers import LinkSerializer


class GetDownloadView(RedirectView):
    permanent = False
    query_string = False

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.username = request.user.username
        else:
            self.username = '**anonymous**'
        session = request.session
        if not session.session_key:
            session.save()
        self.session_key = session.session_key
        return super(GetDownloadView, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        link = get_object_or_404(Link, pk=kwargs.get('pk'))
        link.record_click(session_key=self.session_key,
                          username=self.username)
        return link.url


class LinkViewSet(ReadOnlyModelViewSet):
    queryset = Link.objects.all().prefetch_related('format', 'dataset')
    serializer_class = LinkSerializer


class CsvLinkViewSet(ReadOnlyModelViewSet):
    queryset = Link.objects.filter(
        format__title='CSV').prefetch_related('format', 'dataset')
    serializer_class = LinkSerializer
