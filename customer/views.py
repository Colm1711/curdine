from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustForm
from .models import Profile


def update_user_data(user):
    """
    This function handles Profile details to update and create
    """
    Profile.objects.update_or_create(user=user, defaults={
        'email': user.profile.email,
        'name': user.profile.name,
        'phone_number': user.profile.phone_number,
        'address1': user.profile.address1,
        'address2': user.profile.address2,
        'city': user.profile.city,
        'county': user.profile.county,
        'eir_code': user.profile.eir_code, })

def custForm(request):
    """
    This function handles the saving of data to the database and the view
    presented to the user
    """
    if request.method == 'POST':
        form = CustForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # collect the data from the form to save to the DB
            user.profile.email = form.cleaned_data.get('email')
            user.profile.name = form.cleaned_data.get('name')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.address1 = form.cleaned_data.get('address1')
            user.profile.address2 = form.cleaned_data.get('address2')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.county = form.cleaned_data.get('county')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.eir_code = form.cleaned_data.get('eir_code')
            update_user_data(user)  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # log in the user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home after signing in
            return redirect('index')
    else:
        form = CustForm()

    return render(request, 'signupform.html', {'form': form})
