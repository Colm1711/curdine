from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('menu/', views.Food_item_List.as_view(), name='menu'),
    path('order/', views.Order_form.as_view(), name='order'),
    path('about/', views.About.as_view(), name='about'),
    path('<slug:slug>/', views.Food_Item_View.as_view(), name='food_item'),
    path('delete/<int:pk>/', views.ReviewDeleteView.as_view(),
         name='review_confirm_delete'),
    path('update/<int:pk>/', views.ReviewUpdateView.as_view(), name="update_review"),
    ]
