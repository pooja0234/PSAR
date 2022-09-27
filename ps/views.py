from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Allpost, Profile
from .form import Edit_Blog


# Create your views here.


def index(request):
    posts = Allpost.objects.all()
    return render(request, 'index.html', {
        'posts': posts
    })


def onepost(request, id):
    posts = Allpost.objects.get(id=id)
    return render(request, 'onepost.html', {
        'posts': posts
    })


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already used')
                return redirect('/register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username is already used')
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credential invlid')
            return redirect('/login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def addpost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        images = request.FILES.get('images')
        post = Allpost(title=title, content=content, images=images,
                       user_id=request.user)
        post.save()
        messages.success(request, 'Post has been submitted successfully')
        return redirect('/addpost')
    return render(request, 'addpost.html')


def delete(request, id):
    posts = Allpost.objects.get(id=id)
    posts.delete()
    messages.success(request, 'Post has been deleted')
    return redirect('http://127.0.0.1:8000')


def edit(request, id):
    post = Allpost.objects.get(id=id)
    editblog = Edit_Blog(instance=post)
    if request.method == 'POST':
        form = Edit_Blog(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post has been updated')
            return redirect('http://127.0.0.1:8000')
    return render(request, 'edit_post.html', {'edit_blog': editblog})


def profile(request):
    return render(request, 'profile.html')


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        posts = []
    else:
        poststitle = Allpost.objects.filter(title__icontains=query)
        postscontent = Allpost.objects.filter(content__icontains=query)
        posts = poststitle.union(postscontent)
    return render(request, 'search.html', {
        'posts': posts
    })
