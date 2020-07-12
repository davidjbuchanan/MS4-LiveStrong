from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view show all_products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view show product detail for individual product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
