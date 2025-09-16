from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:cart_item_id>/', views.update_cart, name='update_cart'),    
    path('remove/<int:cart_item_id>/', views.remove_cart_item, name='remove_item'),
]
