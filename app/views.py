from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
  return render(request, "recipes/pages/home.html")

def recipes (request, id):
  return render(request,"recipes/pages/home.html" )