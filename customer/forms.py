from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustForm(UserCreationForm, forms.Form):
    """
    Class is the form that is presented to the user to sign up.

    """


    email = forms.EmailField()
    name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=10)
    address1 = forms.CharField(max_length=50)
    address2 = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    county = forms.CharField(max_length=15)
    eir_code = forms.CharField(max_length=7)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        labels = {'email': 'email',
                  'name': 'name',
                  'phone_number': 'phone_number',
                  'address1': 'address1',
                  'address2': 'address2',
                  'city': 'city',
                  'county': 'county',
                  'eir_code': 'eir_code', }
