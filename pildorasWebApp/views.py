from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home')


def services(request):
    return HttpResponse('Services')


def marketplace(request):
    return HttpResponse('Marketplace')


def blog(request):
    return HttpResponse('Blog')

def contact(request):
    return HttpResponse('Contact')