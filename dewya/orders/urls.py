from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/<int:order_id>/', views.order_success, name='order_success'),
    path('cancel/', views.order_cancel, name='order_cancel'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('track/<int:order_id>/', views.order_tracking, name='order_tracking'),
    path('refund/<int:order_id>/', views.refund_order, name='refund_order'),
    path("", views.order_list, name="order_list"),
    path("track/", views.track_order, name="track_order"),
]
