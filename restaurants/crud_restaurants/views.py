from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_form(req):
    return render(req, 'restaurants/add.html')
def create_restaurant(req, name, address, phone):
    output = f'Added {name} at {address}. Contact them at: {phone}.'
    return HttpResponse(output)
def delete_form(req):
    return render(req, 'restaurants/delete.html')
def delete_restaurant(req, restaurantID):
    output = f'Deleted restaurant number {restaurantID}.'
    return HttpResponse(output)
def restaurants_index(req):
    return render(req, 'restaurants/restaurants.html')
def restaurant_info(req, restaurantID):
    output = f'Viewing page for restaurant {restaurantID}'
    return 
def update_form(req):
    return render(req, 'restaurants/update.html')
def update_restaurant(req, restaurantID):
    output = f'Update form for restaurant {restaurantID}'
    return HttpResponse(output)
def landing_page(req):
    return render(req, 'restaurants/index.html')
def about_page(req):
    return render(req, 'restaurants/about.html')
def base(req):
    return render(req, 'base.html')