from django.urls import path
from .views import index, search_engine

app_name = 'homepage'

urlpatterns = [
    path('', index, name="home"),
    path('search/', search_engine, name="search"),
]