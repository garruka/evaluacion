from django.http import HttpResponse

def vista1(request):
    return HttpResponse("<h1>hola<h1><a>desde la</a><p>la primera app2 y primera vista<p>")

def vista1(request):
    return HttpResponse("<h1>hola<h1><a>desde la</a><p>la primera app2 y segunda vista<p>")