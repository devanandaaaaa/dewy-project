from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .models import Offer , Wishlist , Review
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def product_list(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')

    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        products = products.filter(category__slug=category_slug)

    if search_query:
        products = products.filter(name__icontains=search_query)

    return render(request, 'store/product_list.html', {
        'categories': categories,
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})

def offers_page(request):
    offers = Offer.objects.filter(valid_to__gte=timezone.now())
    return render(request, 'store/offers.html', {'offers': offers})

@login_required
def view_wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'items': items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('store:wishlist')

@login_required
def remove_from_wishlist(request, wishlist_id):
    item = get_object_or_404(Wishlist, id=wishlist_id)
    item.delete()
    return redirect('store:wishlist')

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')
        Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)

    return redirect('store:product_detail', product_id=product_id)
