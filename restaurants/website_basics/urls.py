from django.urls import path
from .views import landing_page
from .views import about_page

urlpatterns = [
    path('', landing_page, name='home'),
    path('about/', about_page, name='about')
]