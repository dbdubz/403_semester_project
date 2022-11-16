from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_form, name='add_form'),
    path('add/<str:name>/<str:address>/<int:phone>/', create_restaurant, name='restaurant_add'),
    path('delete/', delete_form, name='delete_form'),
    path('delete/<int:restaurantID>/', delete_restaurant, name='restaurant_delete'),
    path('restaurants/', restaurants_index, name='all_restaurants'),
    path('restaurants/<int:restaurantID>/', restaurant_info, name='info_page'),
    path('update/', update_form, name='update_form'),
    path('update/<int:restaurantID>/', update_restaurant, name='restaurant_update'),
    path('about/', about_page, name='about'),
    path('', landing_page, name='home'),
]