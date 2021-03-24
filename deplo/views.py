from django.http import HttpResponse
from django.shortcuts import render
def fn(request):
    return render(request, 'home.html')
