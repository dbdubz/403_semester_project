from django.urls import path
from .views import add_form
from .views import create

urlpatterns = [
    path('', add_form, name='add_form'),
    path('<str:name>/<str:address>/<int:phone>/', create, name='submit_form')
]