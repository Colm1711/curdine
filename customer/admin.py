from django.contrib import admin
from .models import Profile

# registering Profile Table to admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''
    This is the class that controls the Admins view of the
    Orders.

    List how the content is presented to Amdmin User and provides list filter
    panel.

    Provides search fields: 'name', 'address1', 'email', 'phone_number', 'city'
    '''
    list_display = ('name', 'address1', 'email', 'phone_number', 'city',)
    search_fields = ['name', 'address1', 'email', 'phone_number', 'city']
    list_filter = ('name', 'address1', 'email', 'phone_number', 'city',)
