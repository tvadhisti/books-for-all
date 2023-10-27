from django.shortcuts import render
from homepage.models import MasterBooks

def book(request):

    context = {
        'title': 'test dulu',
        # 'name': 'Tiva Adhisti Nafira Putri',
    }

    return render(request, "book.html", context)

