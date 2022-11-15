from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_form(req):
    return HttpResponse('Form for restaurant add!')
def create_restaurant(req, name, address, phone):
    output = f'Added {name} at {address}. Contact them at: {phone}.'
    return HttpResponse(output)
def delete_form(req):
    return HttpResponse('Form for restaurant delete!')
def delete_restaurant(req, restaurantID):
    output = f'Deleted restaurant number {restaurantID}.'
    return HttpResponse(output)
def restaurants_index(req):
    return HttpResponse('Index (READ) Page!')
def about_restaurant(req, restaurantID):
    output = f'Viewing page for restaurant {restaurantID}'
    return HttpResponse(output)
def update_form(req):
    return HttpResponse('Update Restaurant Page!')
def update_restaurant(req, restaurantID):
    output = f'Update form for restaurant {restaurantID}'
    return HttpResponse(output)
def landing_page(req):
    return HttpResponse('Main Home Landing Page!')
def about_page(req):
    output = f'About Page'
    return HttpResponse(output)