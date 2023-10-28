from django.shortcuts import render
from .models import MasterBooks
import math
from django.http import JsonResponse

# Create your views here.
def index(request):
    booktype = request.GET.get("type", "")
    
    if booktype == "" :
        bookmst = MasterBooks.objects.all()
    else:
        booktype = [booktype]
        bookmst = MasterBooks.objects.filter(genre__in = booktype)
    row = math.ceil(len(bookmst)/3)
    databooks = []
    for i in range(1,row+1):
        databooks.append(bookmst[(i-1)*3:i*3])

    context = {
        'title' : 'books_for_all',
        'bookmst' : databooks


    }
    return render(request, 'homepage/bottompart.html', context)

def search_engine(request):
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        books = request.POST.get('books')
        print(books)
        # qs = MasterBooks.objects.filter(name__icontains=books)
        # print(qs)
        return JsonResponse({'data': books})
    return JsonResponse({})

