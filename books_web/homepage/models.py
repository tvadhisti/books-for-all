from django.db import models

class MasterBooks(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    url = models.CharField(max_length=255, default='')
    
    # def __str__(self):
    #     return str(self.name)