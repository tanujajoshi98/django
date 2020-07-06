from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cse (request):
    return HttpResponse("Hello from cse")

def mech (request):
    return HttpResponse("Hello from mech")

def entc (request):
    return HttpResponse("Hello from entc")

def civil (request):
    return HttpResponse("Hello from civil")
