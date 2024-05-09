from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    book_list = Book.objects.all()
    context = {
        "book_list":book_list
    }
    return render(request, "books/book.html", context)

def addBook(request):
    form = BookForm()
    context = {'form':form}
    if request.method == 'POST':
        book_title = request.POST['booktitle']
        author = request.POST['author']
        Book(book_title = book_title, author = author).save()
    return render(request, "books/index.html")