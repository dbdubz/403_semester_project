from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_form, name='add_form'),
    path('add/<str:name>/<str:address>/<int:phone>/', create_restaurant, name='submit_form'),
    path('delete/', delete_form, name='delete_form'),
    path('delete/<int:restaurantID>/', delete_restaurant, name='delete_restaurant'),
    path('restaurants/', restaurants_index, name='index_page'),
    path('restaurants/<int:restaurantID>/', about_restaurant, name='info_page'),
    path('update/', update_form, name='update_page'),
    path('update/<int:restaurantID>/', update_restaurant, name='update_restaurant'),
    path('about/', about_page, name='about'),
    path('', landing_page, name='home'),
]