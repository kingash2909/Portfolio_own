import profile

from django.shortcuts import render
from pygments.formatters import img
from django.http import HttpResponse

from .models import Profile


# Create your views here.

def home(request):
    profile = Profile.objects.all()
    return render(request,'home.html', {'profile' : profile})


# def desc(request):
#     return render(request,'Desc.html')

# def cert_redir(request):
#     return HttpResponseRedirect('Desc.html')
