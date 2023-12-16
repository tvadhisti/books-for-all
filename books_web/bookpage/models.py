from django.db import models
from django.contrib.auth.models import User
from homepage.models import MasterBooks

# Create your models here.
class ReviewItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(MasterBooks, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)

    def __str__(self):
        return self.book.title