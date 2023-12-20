from django.urls import path
from . import views

urlpatterns = [
    path('add_question', views.add_question, name="add_question"),
    path('add_answer', views.add_answer, name="add_answer"),
    path('question_view', views.question_view, name="question_view"),
]