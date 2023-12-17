from django.urls import path
from . import create_api, remove_api, get_api

urlpatterns = [
    # url format
    # add
    # path('add/[name_api]/', create_api.add_to_cart_api, name='add_to_cart_api')
    path('login/', create_api.login_user, name='login_api'),
    path('add/create_review/', create_api.create_review, name='create_review_api'),
    path('add/create_wishlist/', create_api.create_wishlist, name='create_wishlist_api'),
    path('add/create_cart/', create_api.create_cart, name='create_cart_api'),
    path('add/create_question/', create_api.create_question, name='create_question_api'),
    path('add/create_answer/', create_api.create_answer, name='create_answer_api'),

    # url format
    # remove
    # path('remove/remove_to_cart/', remove_api.remove_to_cart_api, name='remove_to_cart_api')
    path('remove/remove_cart/<int:book_id>', remove_api.remove_cart, name='remove_cart_api'),
    path('remove/remove_wishlist/<int:book_id>', remove_api.remove_wishlist, name='remove_wishlist_api'),

    # url format
    # get
    # path('get/get_cart/', get_api.get_cart_api, name='get_cart_api')
    path('get/get_homepage_book/', get_api.get_homepage_book, name='get_homepage_book_api'),
    path('get/get_cart/', get_api.get_cart, name='get_cart_api'),
    # path('get/get_answer/<int:question_id>', get_api.get_cart, name='get_answer_api'),
    path('get/get_question_answer/', get_api.get_question_answer, name='get_question_answer_api'),
    path('get/get_review/<int:book_id>', get_api.get_review, name='get_review_api'),
    path('get/get_book/<int:book_id>', get_api.get_book, name='get_book_api'),
]