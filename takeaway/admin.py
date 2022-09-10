from django.contrib import admin
from .models import Food_item
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Food_item)
class Food_itemAdmin(SummernoteModelAdmin):
    '''
    This is the class that controls the Admins view of the
    food items.

    List how the content is presented to Amdmin User and provides list filter 
    panel.

    Provides search fields.

    Slug field is set to autopopulate on food name.
    '''
    list_display = ('food_name', 'description', 'price', 'slug')
    search_fields = ['food_name', 'description', 'price']
    prepopulated_fields = {'slug': ('food_name',)}
    list_filter = ('food_name', 'price')
    summernote_fields = ('description')
