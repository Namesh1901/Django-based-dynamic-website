from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculate():
    x=1
    y=2
    return x+y

def say_hi(request):
    x=calculate()
    return render(request, 'hello.html',{'name':'Namesh'}) 

def add(request):
    val1=request.POST['num1']
    val2=request.POST['num2']
    res=int(val1)+int(val2)
    return render(request,'result.html',{'result':res})