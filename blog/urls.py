# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # 新的URL模式
]
