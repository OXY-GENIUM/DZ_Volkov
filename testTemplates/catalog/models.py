from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40, blank=False)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.price}'

class ProductComment(models.Model):
    full_name = models.CharField(max_length=100, blank=False)  # ФИО
    email = models.EmailField(max_length=100, blank=False)  # Email
    comment = models.TextField(blank=False)  # Текст отзыва
    verified = models.BooleanField(default=False)  # Проверено (чекбокс, по-умолчанию False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Связь с продуктом

    def __str__(self):
        return f'{self.full_name} - {self.product.name} - {self.comment[:30]}...'  # Отображение первых 30 символов отзыва
