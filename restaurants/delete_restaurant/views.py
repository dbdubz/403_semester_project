from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def delete_form(req):
    return HttpResponse('Form for restaurant delete!')
def delete(req, restaurantID):
    output = f'Deleted restaurant number {restaurantID}.'
    return HttpResponse(output)