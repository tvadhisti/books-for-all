from django.shortcuts import render
from homepage.models import MasterBooks
from .models import QuestionItem, AnswerItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect
from django.urls import reverse

@csrf_exempt
def add_question(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            book_id = request.POST['bookid']
            book = MasterBooks.objects.filter(pk=book_id)
            QuestionItem.objects.get_or_create(user=request.user, book=book[0], question=request.POST['question'])
    return HttpResponseRedirect(reverse('question_view'))

@csrf_exempt
def add_answer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            questionid = request.POST['questionid']
            question = QuestionItem.objects.get(pk=questionid)
            AnswerItem.objects.get_or_create(user=request.user, question=question, answer=request.POST['answer'])
    return HttpResponseRedirect(reverse('question_view'))

@login_required(login_url='/auth/login')
def question_view(request):
    question_list = QuestionItem.objects.all()
    answer_buck = []
    for item in question_list:
        temp_buck = [item]
        temp_buck.append(AnswerItem.objects.filter(question=item))
        answer_buck.append(temp_buck)
    context = {
        'question':answer_buck
    }

    return render(request, "question.html", context)