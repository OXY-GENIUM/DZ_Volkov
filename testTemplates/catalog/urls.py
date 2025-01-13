from django.urls import path
from .views import *
from .views import catalog_page

urlpatterns = [
    path('', catalog_page),
    path('add_comment/', add_comment_page),
    path('thanks/', thanks_page, name = "thanks_page"),
    path('reviews/', thanks_page, name = "reviews_page"),
]