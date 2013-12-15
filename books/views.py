#from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from books.models import Book


def index(request):
    books_list = Book.objects.all()
    t = loader.get_template('books/index.html')
    c = Context({'books_list': books_list})
    return HttpResponse(t.render(c))

# Create your views here.
