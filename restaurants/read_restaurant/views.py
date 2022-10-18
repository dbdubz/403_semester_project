from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse('Index (READ) Page!')
def info(req, restaurantID):
    output = f'Viewing page for restaurant {restaurantID}'
    return HttpResponse(output)