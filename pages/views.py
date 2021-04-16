from django.shortcuts import render, redirect
from django.http import HttpResponse

from products.models import Product
from .forms import ProductForm

# Create your views here.
def home_view(request):
    products = Product.objects.filter(featured=True).order_by("id").all()
    form = ProductForm(request.POST or None)
    if form.is_valid():
        cleaned_form = form.cleaned_data
        Product.objects.create(**cleaned_form)
        return redirect('home')
    return render(request, 'home.html', {
        "products": products,
        "form": form,
        })

def contact_view(request):
    return render(request, 'contact.html', {})
