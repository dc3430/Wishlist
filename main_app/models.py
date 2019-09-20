from django.db import models
from django.urls import reverse

# Create your models here.
class Wish(models.Model):
    description = models.TextField(max_length=100)
    quantity = models.IntegerField()
    

    def __str__(self):
      return self.description