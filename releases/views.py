from __future__ import absolute_import, unicode_literals

from django.http import HttpResponsePermanentRedirect, Http404
from django.shortcuts import get_object_or_404, render

from .models import Release


def index(request):
    return render(request, 'releases/download.html')


def redirect(request, version, kind):
    release = get_object_or_404(Release, version=version)
    try:
        redirect_url = release.get_redirect_url(kind)
    except ValueError:
        raise Http404
    return HttpResponsePermanentRedirect(redirect_url)