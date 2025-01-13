from django.http import HttpResponse
from django.shortcuts import render

MENU = {"Главная": "/", "О блоге": "/catalog", "Страница поста": "/about", "Отзывы": "/reviews", "Добавить коментарий": "/catalog/add_comment"}

def main_page(request):
    title = "AI Blog - что это?"
    data = {"menu": MENU, "title": title}  # Передаём саму переменную MENU
    return render(request, "index.html", context=data)


def about_page(request):
    title = "Как сделать игру более привлекательной с помощью VR & AI"
    data = {"menu": MENU, "title": title}
    return render(request, "about.html", context=data)

def reviews_page(request):
    title = "Отзывы"
    data = {"menu": MENU, "title": title}
    return render(request, "reviews.html", context=data)

def add_comment_page(request):
    products = Product.objects.values("id","name")
    title = "Добавить комментарий"
    data = {"menu": MENU, "title": title, "products": products}
    return render(request, "add_comment.html", context=data)
