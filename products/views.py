from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
# Create your views here.
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        product.featured = False
        product.save()
        return redirect('home')
