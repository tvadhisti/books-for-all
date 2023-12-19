from homepage.models import MasterBooks
from bookpage.models import ReviewItem
from wishlist.models import WishlistItem
from question.models import QuestionItem, AnswerItem
from cart.models import CartItem
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.core import serializers

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
            return JsonResponse({"message":"Wrong Method"}, status=400)
    else:
        return JsonResponse({"message":"Unauthenticated"}, status=401)

def get_cart(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            user = request.user
            cartlist_items = CartItem.objects.filter(user=user)
            cartlist_books = [item.book for item in cartlist_items]
            
            json_model = serializers.serialize("json", cartlist_books)
            data = { "cart_list" : json.loads(json_model)}
            return JsonResponse(data)
        else: 
            return JsonResponse({"message":"Wrong Method"}, status=400)
    else:
        return JsonResponse({"message":"Unauthenticated"}, status=401)

def get_question_answer(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            question_list = QuestionItem.objects.all()
            answer_buck = []
            for item in question_list:
                temp_buck = {}
                json_model = serializers.serialize("json", [item])
                temp_buck['question'] = json.loads(json_model)[0]
                get_book_title = MasterBooks.objects.get(pk=temp_buck['question']['fields']['book'])
                temp_buck['question']['fields']['book_title'] = get_book_title.title

                answer = AnswerItem.objects.filter(question=item)
                json_model = serializers.serialize("json", answer)
                temp_buck['answer_list']=json.loads(json_model)
                answer_buck.append(temp_buck)

            data = { "question_answer_list" : answer_buck}
            return JsonResponse(data)
        else: 
            return JsonResponse({"message":"Wrong Method"}, status=400)
    else:
        return JsonResponse({"message":"Unauthenticated"}, status=401)
    
def get_review(request, book_id):
    if request.user.is_authenticated:
        if request.method == "GET":    
            book = MasterBooks.objects.get(pk=book_id)
            review_list = ReviewItem.objects.filter(book=book)
            json_model = serializers.serialize("json", review_list)
            json_model = json.loads(json_model)
            for ind, item in enumerate(json_model):
                user = User.objects.get(pk=int(item['fields']['user']))
                json_model[ind]['fields']['username'] = user.username
            data = { "review_list" :json_model }
            return JsonResponse(data)
        else: 
            return JsonResponse({"message":"Wrong Method"}, status=400)
    else:
        return JsonResponse({"message":"Unauthenticated"}, status=401)

def get_book(request, book_id):
    if request.user.is_authenticated:
        if request.method == "GET":    
            book = MasterBooks.objects.get(pk=book_id)
            json_model = serializers.serialize("json", [book])
            data = { "review_list" : json.loads(json_model)}
            return JsonResponse(data)
        else: 
            return JsonResponse({"message":"Wrong Method"}, status=400)
    else:
        return JsonResponse({"message":"Unauthenticated"}, status=401)

def check_wishlist(request, book_id, user_id):
    if request.method == "GET":    
        book = MasterBooks.objects.get(pk=book_id)
        wish = WishlistItem.objects.filter(book=book, user=user_id)
        if wish:
            json_model = serializers.serialize("json", wish)
            data = json.loads(json_model)
            data[0]['isAdded'] = True
            return JsonResponse(data, status=200, safe=False)
        else:
            return JsonResponse({"isAdded":False}, status=404)
    else: 
        return JsonResponse({"message":"Wrong Method"}, status=400)

def get_wishlist(request):
    if request.user.is_authenticated:
        if request.method == "GET":    
            user = request.user
            wishlist_items = WishlistItem.objects.filter(user=user)
            json_model = serializers.serialize("json", wishlist_items)
            json_model = json.loads(json_model)
            for ind, item in enumerate(json_model):
                book = MasterBooks.objects.get(pk=int(item['fields']['book']))
                json_model[ind]['fields']['book_title'] = book.title

            return JsonResponse({"wishlist_items":json_model}, status=200, safe=False)
        else:
            return JsonResponse({"message":"Wrong Method"}, status=400)
    else: 
        return JsonResponse({"message":"unauthenticated"}, status=401)