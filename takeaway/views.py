from django.shortcuts import render
from django.views import generic
from .models import Food_item


class Food_item_List(generic.ListView):
    model = Food_item
    queryset = Food_item.objects.filter().order_by('-food_name')
    template_name = 'menu.html'
    paginate_by = 6
