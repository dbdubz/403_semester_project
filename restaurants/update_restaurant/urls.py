from django.urls import path
from .views import update
from .views import update_form

urlpatterns = [
    path('', update, name='update_page'),
    path('<int:restaurantID>', update_form, name='update_restaurant')
]