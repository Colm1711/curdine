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
