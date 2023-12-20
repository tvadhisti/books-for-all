from django.shortcuts import render
from .models import WishlistItem
from homepage.models import MasterBooks
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/auth/login')
def wishlist_view(request):
    if request.user.is_authenticated:
        user = request.user
        wishlist_items = WishlistItem.objects.filter(user=user)
        wishlist_books = [item.book for item in wishlist_items]
    else:
        wishlist_books = []

    context = {
        'wishlist_books': wishlist_books
    }
    return render(request, 'wishlist.html', context)

@login_required
def add_to_wishlist(request, book_id):
    if request.user.is_authenticated:
        book = MasterBooks.objects.get(id=book_id)
        # Add the book to the user's wishlist
        WishlistItem.objects.get_or_create(user=request.user, book=book)
        return JsonResponse({'message': 'Book added to wishlist'})
    else:
        return JsonResponse({'message': 'Authentication required to add to wishlist'}, status=401)

def remove_from_wishlist(request, book_id):
    if request.user.is_authenticated:
        book = MasterBooks.objects.get(id=book_id)
        # Find the WishlistItem associated with the user and the book and delete it
        WishlistItem.objects.filter(user=request.user, book=book).delete()
        # Optionally, you can display a success message or perform other actions.
    return JsonResponse({'message': 'Book removed from wishlist'})

