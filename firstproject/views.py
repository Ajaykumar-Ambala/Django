from django.shortcuts import  render
from django.http import HttpResponse
from demoapp.models import Blog1

def home(request):
    post=Blog1.objects.all()
  
    return render(request,"base.html",{'post':post})
def demo(request):
    return render(request,'demo.html')
