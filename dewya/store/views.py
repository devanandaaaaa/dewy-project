from django.shortcuts import render, get_object_or_404
from .models import Product, Category

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

