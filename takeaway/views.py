from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic, View
from .models import Food_item, Order

class Home(TemplateView):
    '''This allows the home page to be rendered to user'''
    template_name = 'index.html'

class Food_item_List(generic.ListView):
    '''This allows the Menu page and items to be rendered to user'''
    model = Food_item
    queryset = Food_item.objects.filter().order_by('-food_name')
    template_name = 'menu.html'
    paginate_by = 6

class Order_form(View):
    '''This allows the Order page and access to Menu items to be rendered to user
       and user to select items to order.
       
       Redirects user to confirmation page with order details and total cost price.

       '''
    # getting menu items to render to the user
    def get(self, request, *args, **kwargs):
        items = Food_item.objects.filter().order_by('-food_name')

        context = {
            'items': items
        }
        return render(request, 'order.html', context)

    def post(self, request, *args, **kwargs):
        # creating order item dictionary with items list
        order_items = {
            'items': []
        }

        # getting items selected
        items = request.POST.getlist('items[]')
        # looping through items to get item id, name and price
        for item in items:
            food_item = Food_item.objects.get(pk__contains=int(item))
            item_data = {
                'id': food_item.pk,
                'name': food_item.food_name,
                'price': food_item.price
            }
            # appending the item to the order_items list inside the order_items dictionary
            order_items['items'].append(item_data)

            # setting price and item_ids list
            price = 0
            item_ids = []

        # looping through selected items to get price and items to overall order
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        # creating the order object    
        order = Order.objects.create(price=price)
        # adding the item_ids list to the item_ids list.
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'order_confirmation.html', context)