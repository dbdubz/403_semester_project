from django.urls import path
from .views import index
from .views import info

urlpatterns = [
    path('', index, name='index_page'),
    path('<int:restaurantID>/', info, name='info_page')
]