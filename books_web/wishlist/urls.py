from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.wishlist_view, name='wishlist_view'),
    path('add_to_wishlist/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist')
]
