from homepage.models import MasterBooks
from bookpage.models import ReviewItem
from wishlist.models import WishlistItem
from question.models import QuestionItem, AnswerItem
from cart.models import CartItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User

@csrf_exempt
def create_review(request):
    if request.method == "POST":
        book_id = request.POST['reviewForm']
        book = MasterBooks.objects.filter(pk=book_id)
        ReviewItem.objects.get_or_create(user=request.user, book=book[0], review=request.POST['review'])
        
        return JsonResponse({"message":"Review Added"}, status=201)
    else:
        return JsonResponse({"message":"Wrong Method"}, status=500)

@csrf_exempt
def create_wishlist(request):
    if request.method == "POST":
        book = MasterBooks.objects.get(id=request.POST['bookid'])
        # Add the book to the user's wishlist
        WishlistItem.objects.get_or_create(user=request.user, book=book)
        return JsonResponse({'message': 'Book added to wishlist'}, status=201)
    else:
        return JsonResponse({"message":"Wrong Method"}, status=500)

@csrf_exempt
def create_cart(request):
    if request.method == "POST":
        book = MasterBooks.objects.get(id=request.POST['bookid'])
        # Add the book to the user's wishlist
        CartItem.objects.get_or_create(user=request.user, book=book)
        return JsonResponse({'message': 'Book added to cart'}, status=201)
    else:
        return JsonResponse({'message': 'Wrong Method'}, status=500)

@csrf_exempt
def create_question(request):
    if request.method == "POST":
        book_id = request.POST['bookid']
        book = MasterBooks.objects.filter(pk=book_id)
        QuestionItem.objects.get_or_create(user=request.user, book=book[0], question=request.POST['question'])
        return JsonResponse({'message': 'Question added!'}, status=201)
    else:
        return JsonResponse({'message': 'Wrong Method'}, status=500)


@csrf_exempt
def create_answer(request):
    if request.method == "POST":
        questionid = request.POST['questionid']
        question = QuestionItem.objects.get(pk=questionid)
        AnswerItem.objects.get_or_create(user=request.user, question=question, answer=request.POST['answer'])
        return JsonResponse({'message': 'Answer added'}, status=201)
    else:
        return JsonResponse({'message': 'Wrong Method'}, status=500)
    
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = {
                'sessionid':request.session._session_key,
                'username':username,
                'userid' : user.id,
                'status':True
            }
            
            return JsonResponse(response, status=201, safe=False)
        else:
            return JsonResponse({'message':'Wrong username and password', 'status':False}, status=401)
    return JsonResponse({'message': 'Wrong Method'}, status=400)

@csrf_exempt
def register(request):
    if request.method == "POST":
        User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        return JsonResponse({"message":"Your account has been created!"}, status=201)
    return JsonResponse({"message":"Bad request! Wrong Method"}, status=400)