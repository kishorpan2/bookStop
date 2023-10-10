from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.TextChoices):
    PROGRAMMING='Programming'
    NETWORKING='Networking'
    SELF_DEVELOPMENT='Self Development'
    MEDICAL='Medical'
    ALGORITHMS='Algorithms'


class Product(models.Model):
    name=models.CharField(max_length=200,default='',blank=False)
    description=models.TextField(max_length=1200,default='',blank=False)
    price=models.DecimalField(max_digits=7, decimal_places=2, default=0)
    brand=models.CharField(max_length=200,default='',blank=False)
    category=models.CharField(max_length=30, choices=Category.choices)
    ratings=models.DecimalField(max_digits=3, decimal_places=2, default=0)
    stock=models.IntegerField(default=0)
    user=models.ForeignKey(User, models.SET_NULL,null=True)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name