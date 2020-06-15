from django.shortcuts import render
from .models import certificate_Details



# Create your views here.

def certificates_page(request):
    certificate = certificate_Details.objects.all()
    return render(request,'Projects.html', {'certificates' : certificate})

