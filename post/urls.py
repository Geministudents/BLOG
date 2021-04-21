# coding=utf-8
from django.conf.urls import url
from django.urls import re_path

from . import views
from .views import *

urlpatterns = [
    re_path(r'^$', views.queryAll),
    re_path(r'^page/(\d+)$', views.queryAll),
    re_path(r'^post/(\d+)$', views.detail),
    re_path(r'^category/(\d+)$',views.queryPostByCid),
    re_path(r'^archive/(\d+)/(\d+)$',views.queryPostByCreated),
]
