from django.contrib import admin
from .models import Food_item, Order
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Food_item)
class Food_itemAdmin(SummernoteModelAdmin):
    '''
    This is the class that controls the Admins view of the
    food items.

    List how the content is presented to Amdmin User and provides list filter 
    panel.

    Provides search fields: 'food_name', 'description', 'price'

    Slug field is set to autopopulate on food name.
    '''
    list_display = ('food_name', 'description', 'price', 'slug')
    search_fields = ['food_name', 'description', 'price']
    prepopulated_fields = {'slug': ('food_name',)}
    list_filter = ('food_name', 'price')
    summernote_fields = ('description')


@admin.register(Order)
class OrderAdmin(SummernoteModelAdmin):
    '''
    This is the class that controls the Admins view of the
    Orders.

    List how the content is presented to Amdmin User and provides list filter 
    panel.

    Provides search fields: 'creation_date', 'name', 'address1','email',
                            'ordered_items','price'
    '''
    list_display = ('creation_date', 'name', 'address1', 'email',
                    'ordered_items', 'price')
    search_fields = ['creation_date', 'name', 'address1', 'email',
                     'ordered_items', 'price']
    list_filter = ('creation_date', 'name', 'address1', 'email', 'price')

    def ordered_items(self, obj):
        """get the food items from list"""
        return ", ".join([i.food_name for i in obj.items.all()])
