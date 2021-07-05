from blogapp import views
from django.urls import path

urlpatterns = [
    path('blog_index', views.blog_index,name='blog_index'),
    path("<int:pk>/", views.blog_detail,name='blog_detail'),


]
