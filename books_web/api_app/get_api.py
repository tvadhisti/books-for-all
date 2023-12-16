from django.shortcuts import render
from homepage.models import MasterBooks
from django.http import JsonResponse
import json
from django.core import serializers

# from .models import ReviewItem
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# @login_required
def get_homepage_book(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            booktype = request.GET.get("type", "")
            if booktype == "" :
                bookmst = MasterBooks.objects.all()
            else:
                booktype = [booktype]
                bookmst = MasterBooks.objects.filter(genre__in = booktype)
            
            json_model = serializers.serialize("json", bookmst)
            data = { "book_list" : json.loads(json_model)}
            return JsonResponse(data)
    else:
        return JsonResponse({"error":401})