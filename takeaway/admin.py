from django.contrib import admin
from .models import Food_item, Order, AboutMe, Review
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

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'food_item', 'creation_date',
                    'approved')
    list_filter = ('approved', 'creation_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
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


@admin.register(AboutMe)
class AboutMeAdmin(SummernoteModelAdmin):
    date_hierarchy = ('date_modified')
    summernote_fields = ('about_text_body')
