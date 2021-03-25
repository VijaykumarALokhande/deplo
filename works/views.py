from django.shortcuts import render

from .models import Work
def home(request):
    objs = Work.objects
    return render(request, 'works.html', {"worklist":objs})
