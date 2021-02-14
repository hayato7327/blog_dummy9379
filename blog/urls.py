from django.urls import path
from . import views
from .admin import mypage_site
from django.conf.urls import url
from django.contrib import admin
from .views import (LikeButton,)


app_name = 'blog'
urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('detail/<int:pk>/', views.Detail.as_view(), name="detail"),
    path('create/', views.Create.as_view(), name="create"),
    path('update/<int:pk>/', views.Update.as_view(), name="update"),
    path('delete/<int:pk>/', views.Delete.as_view(), name="delete"),
     #今回いいねボタンを設置するページ
    path('', views.LikePage, name="like_page"),
     #いいね情報を格納するページ
    path('', LikeButton.as_view(), name='like_api'),
]
