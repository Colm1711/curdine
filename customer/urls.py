from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signupform/', views.cust_form, name='signupform'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout', views.logout, name='logout'),
]
