from django.forms import ModelForm
from wishlist.models import Book

class ProductForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]