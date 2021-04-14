from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view
from products.views import product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('product/<int:id>', product_detail, name='product'),
]
