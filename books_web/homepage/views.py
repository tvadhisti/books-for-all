from django.shortcuts import render
from homepage.models import MasterBooks
import math
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


