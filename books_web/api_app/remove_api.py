from homepage.models import MasterBooks
from cart.models import CartItem
from wishlist.models import WishlistItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def remove_cart(request, book_id):
    if request.method=="DELETE":
        book = MasterBooks.objects.get(id=book_id)
        # Find the CartItem associated with the user and the book and delete it
        CartItem.objects.filter(user=request.user, book=book).delete()
        # Optionally, you can display a success message or perform other actions.
        return JsonResponse({'message': 'Book removed from cart'}, status=202)
    else:
        return JsonResponse({'message': 'Wrong Method'}, status=400)
@csrf_exempt
def remove_wishlist(request, book_id):
    if request.method=="DELETE":
        book = MasterBooks.objects.get(id=book_id)
        # Find the WishlistItem associated with the user and the book and delete it
        WishlistItem.objects.filter(user=request.user, book=book).delete()
        # Optionally, you can display a success message or perform other actions.
        return JsonResponse({'message': 'Book removed from wishlist'}, status=202)
    else:
        return JsonResponse({'message': 'Wrong Method'}, status=400)