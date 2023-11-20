from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request,'hello.html')

def hii(request):
    return render(request,'hii.html')

def hello2(request):
    return render(request,'hello2.html')
