from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
  #chapter3:return HttpResponse("Rango says hey there partner!""<a href='/rango/about/'>About</a>")
  return render(request, 'rango/index.html', context=context_dict)

def about(request):
  return HttpResponse("Rango says here is the about page.""<a href='/rango/'>Index</a>")


