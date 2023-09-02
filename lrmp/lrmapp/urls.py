
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', helloView),
    path('add-book/', addBook, name="addBook"),
    path('add/', add, name="add"),
    path('edit-book/<int:bookId>/', editBook, name="editBook"),
    path('edit/<int:bookId>/', edit, name="edit"),
    path('delete-book/<int:bookId>/', deleteBook, name="deleteBook")
]