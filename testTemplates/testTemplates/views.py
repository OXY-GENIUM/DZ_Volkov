from django.http import HttpResponse
from django.shortcuts import render

MENU = {"Главная": "/", "О блоге": "/catalog", "Страница поста": "/about", "Отзывы": "/reviews"}

def main_page(request):
    title = "AI Blog - что это?"
    data = {"menu": MENU, "title": title}  # Передаём саму переменную MENU
    return render(request, "index.html", context=data)

def catalog_page(request):
    title = "О блоге"
    data = {"menu": MENU, "title": title}
    return render(request, "catalog.html", context=data)

def about_page(request):
    title = "Как сделать игру более привлекательной с помощью VR & AI"
    data = {"menu": MENU, "title": title}
    return render(request, "about.html", context=data)

def reviews_page(request):
    title = "Отзывы"
    data = {"menu": MENU, "title": title}
    return render(request, "reviews.html", context=data)
