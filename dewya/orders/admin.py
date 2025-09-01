from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'status', 'total_amount', 'created')
    list_filter = ('status', 'created')
    readonly_fields = ('stripe_payment_intent_id', 'stripe_payment_status')


