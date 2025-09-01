from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from store.models import Product

def _get_session_key(request):
    if request.user.is_authenticated:
        return None
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)

        if request.user.is_authenticated:
            item, created = CartItem.objects.get_or_create(
                user=request.user, product=product,
                defaults={'quantity': quantity}
            )
            if not created:
                item.quantity += quantity
                item.save()
        else:
            session_key = _get_session_key(request)
            item, created = CartItem.objects.get_or_create(
                session_key=session_key, product=product,
                defaults={'quantity': quantity}
            )
            if not created:
                item.quantity += quantity
                item.save()
        return redirect('cart:view_cart')
    return redirect('store:product_list')

def view_cart(request):
    if request.user.is_authenticated:
        items = CartItem.objects.filter(user=request.user)
    else:
        session_key = _get_session_key(request)
        items = CartItem.objects.filter(session_key=session_key)

    total = sum([item.get_total_price() for item in items])
    return render(request, 'cart/cart.html', {'items': items, 'total': total})
