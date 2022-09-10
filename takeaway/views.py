from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Food_item

class Home(TemplateView):
    '''This allows the home page to be rendered to user'''
    template_name = 'index.html'

class Food_item_List(generic.ListView):
    '''This allows the Menu page and ittems to be rendered to user'''
    model = Food_item
    queryset = Food_item.objects.filter().order_by('-food_name')
    template_name = 'menu.html'
    paginate_by = 6
