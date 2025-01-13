
from django.shortcuts import render
from .models import Product, ProductComment
MENU = {"Главная": "/", "О блоге": "/catalog", "Страница поста": "/about", "Отзывы": "/reviews", "Добавить коментарий": "/catalog/add_comment"}


def catalog_page(request):
    products = Product.objects.all()
    title = "О блоге"
    data = {"menu": MENU, "title": title, "products": products}
    return render(request, "catalog.html", context=data)


def add_comment_page(request):
    products = Product.objects.values("id","name")
    title = "Добавить комментарий"
    data = {"menu": MENU, "title": title, "products": products}
    return render(request, "add_comment.html", context=data)

def thanks_page(request):
    user_name = request.POST['user_name']
    comment = request.POST['comment']
    product = Product.objects.get(pk=request.POST['product'])
    ProductComment.objects.create(user_name=user_name, comment=comment, product=product)
    title = "Страница благодарностей"
    data = {"menu": MENU, "title": title,"user_name":user_name}
    return render(request, "thanks.html", context=data)



