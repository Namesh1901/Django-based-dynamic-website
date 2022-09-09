from django.shortcuts import render
from .models import destination
from django.http import HttpResponse
# Create your views here.
def index(request):
    dests=destination.objects.all()
    return render(request, 'index.html',{'destlst':dests}) 
def destine(request):
    destname=request.POST.get("VAL1","")
    dests=destination.objects.all()
    print(destname)
    return render(request,'destination.html',{'destlt':dests,'dest':destname})