from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(req):
    return HttpResponse('Main Home Landing Page!')
def about_page(req):
    output = f'About Page'
    return HttpResponse(output)