from django.shortcuts import render
from . models import Build

# Create your views here.
def build(request):
    builds = Build.objects
    return render(request, 'builds/builds.html', {'builds':builds})