from django.db import models
from django.conf import settings
from store.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    stripe_payment_intent_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_payment_status = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, default="Processing warehouse")

    def __str__(self):
        return f"Order {self.id} - {self.full_name}"

