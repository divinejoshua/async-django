from django.urls import path, include
from . import views

app_name = "blog_api"

urlpatterns = [
    path('sync', views.BlogView.as_view(), name='blog_view_sync'),                       #Check user api
    path('async', views.BlogAsyncView.as_view(), name='blog_view_async'),                       #Check user api
]