from django.urls import path
from . import create_api, remove_api, get_api

urlpatterns = [
    # url format
    # add
    # path('add/[name_api]/', create_api.add_to_cart_api, name='add_to_cart_api')

    # url format
    # remove
    # path('remove/remove_to_cart/', remove_api.remove_to_cart_api, name='remove_to_cart_api')

    # url format
    # get
    # path('get/get_cart/', get_api.get_cart_api, name='get_cart_api')
    path('get/get_homepage_book/', get_api.get_homepage_book, name='get_homepage_book_api')
]