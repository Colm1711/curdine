from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='index/'),
    path('menu/', views.Food_item_List.as_view(), name='menu/'),
]
