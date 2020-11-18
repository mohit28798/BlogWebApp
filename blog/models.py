
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class category(models.Model):
    categories=models.CharField(max_length=60, unique=True)
    
    def __str__(self):
        return self.categories
class post(models.Model):
    
    cate=models.ForeignKey(category, on_delete=models.CASCADE)
    heading=models.CharField(max_length=60)
    thumb=models.ImageField(blank=True)
    disc=models.TextField()
    footer=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


class comment(models.Model):
    comment=models.TextField()
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    postid=models.ForeignKey(post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
   
    
class archives(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    postid=models.ForeignKey(post, on_delete=models.CASCADE)
    
class feedbacks(models.Model):
    firstname=models.CharField(max_length=60)
    lastname=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=15)
    message=models.TextField()
    
    
    
     
