"""mysite URL Configuration

[...]
"""
from django.contrib import admin
from blog import views
from django.conf.urls import url
urlpatterns = [
    url('admin/', admin.site.urls),
    url('', views.post_list, name='post_list'),
    url('post/<int:pk>/', views.post_detail, name='post_detail'),
]