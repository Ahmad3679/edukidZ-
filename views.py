from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

from django.http import HttpResponse

def buy_product(request, product_id):
    if request.method == 'POST':
        # هنا ممكن تضيف أي معالجة لاحقًا
        return HttpResponse(f"تم شراء المنتج رقم {product_id} بنجاح ✅")