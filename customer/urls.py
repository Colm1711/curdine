from . import views
from django.urls import path

urlpatterns = [
    path('signupform/', views.custForm, name='signupform')
]