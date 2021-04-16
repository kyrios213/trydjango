from django import forms

from products.models import Product

class ProductForm(forms.Form):
    title = forms.CharField(label='Title', max_length=120)
    description = forms.CharField(label='Description', max_length=500, required=False, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    price = forms.DecimalField(label='Price', max_digits=100, decimal_places=2)
    summary = forms.CharField(label='Summary', max_length=500, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
