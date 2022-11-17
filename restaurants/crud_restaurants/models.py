from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class State(models.Model):
    state_abbr = models.CharField(primary_key=True, max_length=2)
    state_name = models.CharField(max_length=20)
    def __str__(self):
        return (self.state_info)
    
    @property
    def state_info(self):
        return (self.state_abbr)
    
    class Meta:
        db_table = 'state'

"""
class ZipCode(models.Model):
    zip_code = models.CharField(max_length=5)
    zip_state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return (self.zip_code)
"""

class City(models.Model):
    city_name = models.CharField(max_length=30)
    city_state = models.ForeignKey(State, null=True, on_delete=models.DO_NOTHING)
    #city_zip = models.CharField(max_length=5)

    def __str__(self):
        return (self.city_info)

    @property
    def city_info(self):
        return (self.city_name)

    class Meta:
        db_table = 'city'

class RestaurantType(models.Model):
    restaurant_type = models.CharField(max_length=20)
    def __str__(self):
        return (self.restaurant_type)
    
    class Meta:
        db_table = 'restaurant_type'

class RestaurantStyle(models.Model):
    restaurant_type = models.ForeignKey(RestaurantType, null=True, on_delete=models.SET_NULL)
    restaurant_style = models.CharField(max_length=30)
    def __str__(self):
        return (self.restaurant_specs)

    @property
    def restaurant_specs(self):
        return '%s - %s' % (self.restaurant_style, self.restaurant_type)

    class Meta:
        db_table = 'restaurant_style'

class Restaurant(models.Model):
    restaurant_type_style = models.ForeignKey(RestaurantStyle, null=True, on_delete=models.SET_NULL)
    restaurant_name = models.CharField(max_length=30)
    restaurant_street = models.CharField(max_length=30)
    restaurant_city = models.ForeignKey(City, null=True, on_delete=models.DO_NOTHING)
    restaurant_state = models.ForeignKey(State, null=True, on_delete=models.DO_NOTHING)
    restaurant_zip = models.CharField(max_length=5)
    restaurant_image = models.ImageField(null=True)
    def __str__(self):
        return (self.restaurant_info)
    
    @property
    def restaurant_info(self):
        return '%s - %s' % (self.restaurant_name, self.restaurant_street)

    class Meta:
        db_table = 'restaurant'

    @property
    def address_info(self):
        return '%s, %s, %s, %i' % (self.restaurant_street, self.restaurant_city, self._state, self.restaurant_zip)

class MenuItem(models.Model):
    item = models.CharField(max_length=30)
    restaurant = models.ManyToManyField(Restaurant)
    description = models.CharField(max_length=3000, blank=True)
    def __str__(self):
        return (self.item_info)
    
    @property
    def item_info(self):
        return (self.item)

    class Meta:
        db_table = 'menu_item'
    
class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    user_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 13, blank = True)
    restaurants_visited = models.ManyToManyField(Restaurant, blank = True)
    food_tried = models.ManyToManyField(MenuItem, blank=True)
    def __str__(self):
        return (self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'user'