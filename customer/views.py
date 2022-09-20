from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustForm, CustUpdateForm, ProfileUpdateForm
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


def cust_form(request):
    """
    This function handles the saving of data to the database and the view
    presented to the user.

    If user fills in details they will be signed in and redirect to the home page
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
            messages.success(request,
                             "Thank you for signing up for our site!")
            # redirect user to home after signing in
            return redirect('index')
    else:
        form = CustForm()

    return render(request, 'signupform.html', {'form': form})


def logout(request):
    """
    This function handles user log out and redirects to the home page
    """
    auth_logout(request)
    messages.error(request, "You have logged out. See you later :)")
    return HttpResponseRedirect('/')


@login_required
def update_profile(request):
    """
    This function handles rendering of the update page to the user
    and logic to update.

    User must be signed in to do this.
    """
    if request.method == 'POST':
        # passing in instance so form doesn't render empty
        user_form = CustUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('update_profile')
        else:
            messages.error(request, "Your profile has not been updated!!!")
    else:
        user_form = CustUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    }

    return render(request, 'profile_update.html', context)

@login_required
def delete_user(request):
    """
    This function handles user account deletion on the user update page
    and redirects to the home page
    """
    user = User.objects.filter(id=request.user.id)
    user.delete()
    messages.error(request, "Your profile has been deleted we are sorry to see you go!")
    return HttpResponseRedirect('/')