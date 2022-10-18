from django.urls import path
from .views import delete_form
from .views import delete

urlpatterns = [
    path('', delete_form, name='delete_form'),
    path('<int:restaurantID>/', delete, name='delete_restaurant')
]