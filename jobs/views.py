from django.shortcuts import render

from .models import Job
def home(request):
    objs = Job.objects
    return render(request, 'home.html', {"listofjobs":objs})
