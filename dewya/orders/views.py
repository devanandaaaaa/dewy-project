import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from cart.models import CartItem
from .models import Order
from django.urls import reverse
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    if not items:
        return redirect('store:product_list')

    total = sum([item.get_total_price() for item in items])  
    total_paise = int(total * 100)  

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            email=email,
            address=address,
            total_amount=total,
            status='pending'
        )

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {'name': 'The Dewy Ritual Order'},
                    'unit_amount': total_paise,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('orders:order_success', args=[order.id])),
            cancel_url=request.build_absolute_uri(reverse('orders:order_cancel')),
        )

        return redirect(session.url, code=303)

    return render(request, 'orders/checkout.html', {
        'items': items,
        'total': total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status != 'paid':
        order.status = 'paid'
        order.save()

    CartItem.objects.filter(user=request.user).delete()
    return render(request, 'orders/order_success.html', {'order': order})

def payment_success(request):
    order_id = request.session.get('order_id')
    order = Order.objects.get(id=order_id)
    order.status = 'paid'
    order.save()
    send_mail(
        subject=f"Your order #{order.id} confirmation - The Dewy Ritual",
        message=f"Hi {order.full_name},\n\n"
                f"Thank you for your order #{order.id}. Your payment has been received successfully.\n\n"
                f"Order Details:\n"
                f"- Amount Paid: ₹{order.total_amount}\n"
                f"- Status: {order.status}\n\n"
                f"You can track your order in your account anytime.\n\n"
                f"Regards,\nThe Dewy Ritual Team",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[order.email],
        fail_silently=False,
    )

    return render(request, 'orders/order_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/my_orders.html', {'orders': orders})

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session['metadata']['order_id']
        try:
            order = Order.objects.get(id=order_id)
            order.status = 'paid'
            order.save()
        except Order.DoesNotExist:
            pass

    return HttpResponse(status=200)

@login_required
def order_tracking(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_tracking.html', {'order': order})

def order_cancel(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    order.status = 'cancelled'
    order.save()
    
    return render(request, 'orders/order_cancel.html', {'order': order})

@login_required
def refund_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.status = 'refunded'
    order.save()

    return render(request, 'orders/order_refunded.html', {'order': order})
