from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #APIs to post a comment
    path('postComment',views.postComment,name="postComment"), 

    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),#slug in url will be string used in blogPost of blog's views
]
