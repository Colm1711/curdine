from django.db import models
from cloudinary.models import CloudinaryField


class Food_item(models.Model):
    '''
    This is the food item model for items that user will
    be able order from the website
    '''
    food_name = models.CharField(max_length=200, unique=True)
    food_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-food_name']
    
    def __str__(self):
        return self.food_name


class Order(models.Model):
    '''
    This is the order model for the user to
    be able to submit order from the website with items and address.

    '''
    creation_date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(
        'Food_item', related_name='order', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    email = models.EmailField(null=False)
    name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=15, blank=True)
    eir_code = models.CharField(max_length=7, blank=True)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return f'Order: {self.creation_date.strftime("%m%d%Y, %H:%M:%S")}'
