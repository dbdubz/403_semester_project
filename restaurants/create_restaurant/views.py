from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_form(req):
    return HttpResponse('Form for restaurant add!')
def create(req, name, address, phone):
    output = f'Added {name} at {address}. Contact them at: {phone}.'
    return HttpResponse(output)