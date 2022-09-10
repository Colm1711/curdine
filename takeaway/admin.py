from django.contrib import admin
from .models import Food_item
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Food_item)
class Food_itemAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
