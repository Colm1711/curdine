from . import views
from django.urls import path

urlpatterns = [
    path('signupform/', views.cust_form, name='signupform')
]
