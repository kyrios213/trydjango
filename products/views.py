from django.shortcuts import render

from .models import Product
# Create your views here.
def product_detail(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request, 'detail.html', {'product': product})
