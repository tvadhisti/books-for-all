from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'books_for_all'
    }
    return render(request, 'homepage/index.html', context)