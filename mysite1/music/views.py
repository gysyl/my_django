from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
    return HttpResponse("Hello, this is page 1.")
def page2(request):
    return HttpResponse("Hello, this is page 2.")
def page3(request):
    return HttpResponse("Hello, this is page 3.")