from django.db import models
from django.contrib.auth.models import User
from homepage.models import MasterBooks

# Create your models here.
class QuestionItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(MasterBooks, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)

    def __str__(self):
        return self.book.title
    
class AnswerItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionItem, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.book.title