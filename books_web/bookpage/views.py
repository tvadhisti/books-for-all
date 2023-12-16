from django.shortcuts import render
from homepage.models import MasterBooks
from .models import ReviewItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/auth/login')
def book(request, book_id):
    book = MasterBooks.objects.get(pk=book_id)
    review_list = ReviewItem.objects.filter(book=book).filter(user=request.user) 
    context = {
        'book':book,
        'review':review_list
        # 'name': 'Tiva Adhisti Nafira Putri',
    }

    return render(request, "book.html", context)

@csrf_exempt
def review(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            book_id = request.POST['reviewForm']
            book = MasterBooks.objects.filter(pk=book_id)
            ReviewItem.objects.get_or_create(user=request.user, book=book[0], review=request.POST['review'])
    return HttpResponseRedirect(reverse('book_view', kwargs={'book_id': book_id})+"#reviewElement")