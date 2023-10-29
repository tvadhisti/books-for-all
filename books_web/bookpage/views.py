from django.shortcuts import render
from homepage.models import MasterBooks
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login')
def book(request, book_id):
    book = MasterBooks.objects.filter(pk=book_id)
    context = {
        'book':book[0]
        # 'name': 'Tiva Adhisti Nafira Putri',
    }

    return render(request, "book.html", context)

