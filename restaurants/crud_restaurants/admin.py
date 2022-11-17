from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(ZipCode)
admin.site.register(State)
admin.site.register(City)
admin.site.register(RestaurantType)
admin.site.register(RestaurantStyle)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(User)