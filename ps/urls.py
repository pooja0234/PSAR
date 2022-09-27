from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('onepost/<int:id>', views.onepost, name='post'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('addpost', views.addpost, name='addpost'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('profile', views.profile, name='profile'),
    path('search', views.search, name='search'),


]
