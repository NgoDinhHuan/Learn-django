from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here.
def home(request):
    t = tong()
    h = hieu()
    data = {
        "tong":t,
        "hieu":h
    }
    return render(request,"demo/index.html", data) 

def tong():
    return 10 + 20 

def hieu():
    return 10-20