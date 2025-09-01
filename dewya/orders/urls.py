from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/<int:order_id>/', views.order_success, name='order_success'),
    path('cancel/', views.order_cancel, name='order_cancel'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),
]



