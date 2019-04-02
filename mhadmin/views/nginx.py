from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from urllib.parse import quote


def check(request):
    """ Checks if a user is authenticated """
    if request.user and request.user.is_authenticated:
        return HttpResponse("Authorized")
    else:
        return HttpResponse('Unauthorized', status=401)


def check_staff(request):
    """ Checks if a user is authenticated """

    if request.user and request.user.is_authenticated and request.user.is_staff:
        return HttpResponse("Authorized")
    else:
        return HttpResponse('Unauthorized', status=401)


def authenticate(request):
    """ Renders a login view that respects the "X-Original-URI" header. """

    url = "{}?next={}".format(
        settings.LOGIN_URL,
        quote(request.META.setdefault("HTTP_X_ORIGINAL_URI", ""))
    )
    return HttpResponseRedirect(url)


def authenticate_staff(request):
    """ Renders a login view that respects the "X-Original-URI" header. """

    url = "{}?next={}".format(
        settings.LOGIN_STAFF_URL,
        quote(request.META.setdefault("HTTP_X_ORIGINAL_URI", ""))
    )
    return HttpResponseRedirect(url)
