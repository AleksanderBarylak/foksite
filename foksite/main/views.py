from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'main/homepage.html')
# Create your views here.
