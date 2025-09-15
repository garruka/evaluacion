from django.http import HttpResponse
def vista1(request):
 return HttpResponse("<h1>App1 - Vista1</h1><p>Hola  App1/Vista1</p><a>todo bien</a>")
def vista2(request):
 return HttpResponse("<h1>App1 - Vista2</h1><p>Hol App1/Vista2</p><a>todo bien</a>")
