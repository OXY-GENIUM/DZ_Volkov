
from django.shortcuts import render
from .models import Product

MENU = {"Главная": "/", "О блоге": "/catalog", "Страница поста": "/about", "Отзывы": "/reviews"}


def catalog_page(request):
    products = Product.objects.all()
    title = "О блоге"
    data = {"menu": MENU, "title": title, "products": products}
    return render(request, "catalog.html", context=data)
