from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic, View
from django.core.mail import send_mail
from .models import Food_item, Order, AboutMe
from .forms import ReviewForm


class Home(TemplateView):
    '''This allows the home page to be rendered to user'''
    template_name = 'index.html'


class About(generic.ListView):
    '''This allows the about page to be rendered to user'''
    model = AboutMe
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_text_body'] = AboutMe.objects.values_list(
            'about_text_body', flat=True)
        return context


class Food_item_List(generic.ListView):
    '''
    This allows the Menu page and items to be rendered to user
    '''
    model = Food_item
    queryset = Food_item.objects.filter().order_by('-food_name')
    template_name = 'menu.html'
    paginate_by = 6


class Food_Item_View(View):
    '''
    This allows user to navigate to food item to leave review.
    '''
    def get(self, request, slug, *args, **kwargs):
        item = get_object_or_404(Food_item, slug=slug)
        reviews = item.reviews.filter(approved=True).order_by('-creation_date')
        context = {   
                    'item': item,
                    'reviews': reviews,
                    'reviewed': False,
                    'review_form': ReviewForm(),
                    }

        return render(request, 'food_item.html', context)

    def post(self, request, slug, *args, **kwargs):
        item = get_object_or_404(Food_item, slug=slug)
        reviews = item.reviews.filter(approved=True).order_by('-creation_date')

        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.food_item_id = item
            review_form.instance.email = request.user.profile.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.food_item = item
            review.save()
        else:
            review_form = ReviewForm()

        context = {
                'item': item,
                'reviews': reviews,
                'reviewed': True,
                'review_form': review_form,
            }

        return render(request, "food_item.html", context,)


class Order_form(View):
    '''
        This allows the Order page and access to Menu items to be rendered 
        to user and user to select items to order.
       
        Redirects user to confirmation page with order details and total 
        cost price.

       '''
    # getting menu items to render to the user
    def get(self, request, *args, **kwargs):
        items = Food_item.objects.filter().order_by('-food_name')

        context = {
            'items': items
        }
        return render(request, 'order.html', context)

    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        county = request.POST.get('county')
        eir_code = request.POST.get('eir_code')

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
            # appending the item to the order_items list inside the
            # order_items dictionary
            order_items['items'].append(item_data)

            # setting price and item_ids list
            price = 0
            item_ids = []

        # looping through selected items to get price and items to
        # overall order
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        # creating the order object    
        order = Order.objects.create(
            price=price,
            name=name,
            email=email,
            phone_number=phone_number,
            address1=address1,
            address2=address2,
            county=county,
            city=city,
            eir_code=eir_code,
            )
        # adding the item_ids list to the item_ids list.
        order.items.add(*item_ids)
        
        # send confirmation email
        # unpack the order items to add to list
        ordered_item = []
        for i in order_items['items']:
            ordered_item.append(i['name'])

        # email body
        body = ('Your order is being processed and with the kitchen crew!\n'
                f'Your order: {ordered_item}\n'
                f'Your total price to pay: €{price}')
        
        # email details
        send_mail(
            'Thank you for your order!',
            body,
            'example@example.com',
            [email]
        )

        context = {
            'items': order_items['items'],
            'price': price,
            'user': [
                name,
                email,
                phone_number,
                address1,
                address2,
                county,
                city,
                eir_code,
            ]
        }

        return render(request, 'order_confirmation.html', context)
