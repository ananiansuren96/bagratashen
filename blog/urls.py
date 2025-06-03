from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('new/', views.post_create, name='post_create'),
    path('register/', views.register, name='register'),
]
