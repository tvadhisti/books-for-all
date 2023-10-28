from django.shortcuts import render
from homepage.models import MasterBooks

def book(request, book_id):
    book = MasterBooks.objects.filter(pk=book_id)
    context = {
        'title': 'test dulu',
        'book':book[0]
        # 'name': 'Tiva Adhisti Nafira Putri',
    }

    return render(request, "book.html", context)

