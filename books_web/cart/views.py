from django.shortcuts import render
from .models import CartItem
from homepage.models import MasterBooks
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import math

# Create your views here.
@login_required(login_url='/auth/login')
def cart_view(request):
    if request.user.is_authenticated:
        user = request.user
        cartlist_items = CartItem.objects.filter(user=user)
        cartlist_books = [item.book for item in cartlist_items]
    else:
        cartlist_books = []
    
    row = math.ceil(len(cartlist_books)/2)
    databooks = []
    for i in range(1,row+1):
        databooks.append(cartlist_books[(i-1)*3:i*3])

    context = {
        'cartlist_books': databooks
    }
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request, book_id):
    if request.user.is_authenticated:
        book = MasterBooks.objects.get(id=book_id)
        # Add the book to the user's wishlist
        CartItem.objects.get_or_create(user=request.user, book=book)
        return JsonResponse({'message': 'Book added to cart'})
    else:
        return JsonResponse({'message': 'Authentication required to add to cart'}, status=401)
    
def remove_from_cart(request, book_id):
    if request.user.is_authenticated:
        book = MasterBooks.objects.get(id=book_id)
        # Find the CartItem associated with the user and the book and delete it
        CartItem.objects.filter(user=request.user, book=book).delete()
        # Optionally, you can display a success message or perform other actions.
    return JsonResponse({'message': 'Book removed from cart'})
