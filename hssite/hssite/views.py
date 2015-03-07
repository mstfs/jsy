from django.http import HttpResponse

def hello(request):
	return HttpResponse("<h2>Hello Word...<h2>")