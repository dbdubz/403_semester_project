from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def update(req):
    return HttpResponse('Update Restaurant Page!')
def update_form(req, restaurantID):
    output = f'Update form for restaurant {restaurantID}'
    return HttpResponse(output)