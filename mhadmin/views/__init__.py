from django.http import HttpResponse

def healthcheck(request):
    """ Renders a simple healthcheck request """

    return HttpResponse("ok")