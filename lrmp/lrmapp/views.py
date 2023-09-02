from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import *

# Create your views here.
def helloView(request):

    books = Book.objects.all()

    return render(request, "viewBook.html", {'books' : books})

def addBook(request):

    return render(request, "addBook.html")

def add(request):

    if request.method == "POST":

        t = request.POST["title"]
        p = request.POST["price"]

        book = Book()
        book.title = t
        book.price = p
        book.save()
        return HttpResponseRedirect('/')
    
def editBook(request, bookId):
    
    book = Book.objects.get(id=bookId)

    return render(request, "editBook.html", {"book":book})

def edit(request, bookId):

    if request.method == "POST":

        t = request.POST["title"]
        p = request.POST["price"]

        book = Book.objects.get(id = bookId)
        book.title = t
        book.price = p
        book.save()
        return HttpResponseRedirect('/')
    
def deleteBook(request, bookId):
    
    book = Book.objects.get(id = bookId)
    book.delete()

    return HttpResponseRedirect("/")