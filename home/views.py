from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def homeView(request):
    profile = Profile.objects.all()
    context = {'profile':profile}
    return render(request, 'home/home.html', context)
