from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .models import *
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib import messages
import re



def subscribe(request):
    if request.method=="POST":
        reciver=request.POST['email']
        send_mail("myblog subscription",
                  "hey! welcome to myblog socity . we will keep you updated",
                   settings.EMAIL_HOST_USER, 
                   [reciver], 
                   fail_silently=False)
    return render(request,'index.html')


def feedback(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        new=feedbacks(firstname=firstname,lastname=lastname,email=email,phone=phone, message=message)
        new.save()
        messages.info(request,"thanks for feedback")
        return redirect('contact')




def archive(request,pk):
    if request.method=="GET":
        post1=get_object_or_404(post, id=pk)
        new=archives(username=request.user,postid=post1)
        new.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def archived(request):
    username=request.user.username
    select=archives.objects.filter(username=request.user)
    return render(request,'archived.html',{'result':select,'username':username})        


def loginaccount(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid user')
            return redirect('login')

def createaccount(request):
     if request.method=="POST":
         first_name=request.POST['first_name']
         last_name=request.POST['last_name']
         username=request.POST['username']
         email=request.POST['email']
         password=request.POST['password']
         confirmpassword=request.POST['confirmpassword']
         if password==confirmpassword:
             if User.objects.filter(username=username).exists():
                 messages.info(request,"username taken")
                 return redirect("login")
         new=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password , is_staff=True)
         new.save()
         return redirect("login")
         



def selectcategory(request):
    category1=category.objects.all().order_by('categories')
    return render(request,'selectcategory.html',{'category':category1,})




def search(request):
    search=request.POST["searchtext"]
    posts=post.objects.filter(heading__contains=search)
    return render(request,'search.html',{'result':posts})

def logout(request):
    auth.logout(request)
    return redirect('home')



def home(request):
    
    ads=post.objects.filter(cate=6).order_by('-created_date')[:2]
    posts=post.objects.exclude(cate=6).order_by('-created_date')[:10]
    return render(request,'index.html',{'result':posts ,'ads':ads})


def shuffle(request):
    
    ads=post.objects.filter(cate=6).order_by('-created_date')[:2]
    posts=post.objects.exclude(cate=6).order_by('?')[:10]
    return render(request,'index.html',{'result':posts ,'ads':ads})


def login(request):

    return render(request,'login.html')

def signup(request):

    return render(request,'signup.html')

def singleblog(request,pk):
    if request.method=="POST":
        comment1=request.POST['message']
        with open("blog/words.txt",'r')as f:
            words=[word for line in f for word in line.split(",")]
        
        word1=comment1.split()
        i=0
        for x in word1:
            if x in words:
                i=1
        if i==0:
            post1=get_object_or_404(post, id=pk)
            new=comment(comment=comment1,username=request.user,postid=post1)
            new.save()
            blog=post.objects.filter(pk=pk)
            comm=comment.objects.filter(postid=pk)
            
            return render(request,'blog-single.html',{'result':blog, 'com':comm })
            
            
        else:
            blog=post.objects.filter(pk=pk)
            comm=comment.objects.filter(postid=pk)
            messages.info(request,"your comment cant be taken")
            return render(request,'blog-single.html',{'result':blog, 'com':comm })
           
    else:
        blog=post.objects.filter(pk=pk)
        comm=comment.objects.filter(postid=pk)
        return render(request,'blog-single.html',{'result':blog, 'com':comm })

def filtered(request,pk):
    posts=post.objects.filter(cate=pk).order_by('-created_date')
    return render(request,'business.html',{'result':posts})


def accounts(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')
