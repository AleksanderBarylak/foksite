from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("123")        #return html here

# Create your views here.
