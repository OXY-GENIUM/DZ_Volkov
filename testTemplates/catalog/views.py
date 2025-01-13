
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
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        comment = request.POST['comment']
        product = Product.objects.get(pk=request.POST['product'])

        # Проверяем, был ли отправлен чекбокс
        verified = 'verified' in request.POST  # Чекбокс будет присутствовать, если он отмечен

        # Создаем комментарий
        ProductComment.objects.create(
            full_name=full_name,
            email=email,
            comment=comment,
            verified=verified,  # Сохраняем значение чекбокса
            product=product
        )

        title = "Страница благодарностей"
        data = {"menu": MENU, "title": title, "user_name": full_name,
                "verified": verified}  # Передаем также значение verified
        return render(request, "thanks.html", context=data)

    return render(request, "error.html", {"message": "Некорректный запрос."})






