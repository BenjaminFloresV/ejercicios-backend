from pyexpat import model
from django.db import models

# Create your models here.

class Cat(models.Model):
    cat_name=models.CharField(max_length=150)
    cat_race=models.CharField(max_length=150)
    cat_age=models.IntegerField()
    cat_genre=models.CharField(max_length=120)
    cat_color=models.CharField(max_length=50)
    cat_weight=models.CharField(max_length=50)
