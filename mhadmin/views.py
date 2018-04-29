from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse

from urllib.parse import quote

def healthcheck(request):
    """ Renders a simple healthcheck request """

    return HttpResponse("ok")

def authenticate(request):
    """ Renders a login view that respects the "X-Original-URI" header. """
    
    url = "{}?next={}".format(
        reverse('admin:login'), 
        quote(request.META.setdefault("HTTP_X_ORIGINAL_URI", ""))
    )
    return HttpResponseRedirect(url)


def check(request):
    """ Checks if a user is authenticated """
    if request.user and request.user.is_authenticated:
        return HttpResponse("Authorized")
    else:
        return HttpResponse('Unauthorized', status=401)

