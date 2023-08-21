from django.shortcuts import render, HttpResponse

# Create your views here.
def secondPage(request):
    return HttpResponse('hello second page')