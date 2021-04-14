from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product
from .forms import ProductForm

# Create your views here.
def home_view(request):
    products = Product.objects.filter(featured=True).all()
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'home.html', {
        "products": products,
        "form": form,
        })

def contact_view(request):
    return render(request, 'contact.html', {})
