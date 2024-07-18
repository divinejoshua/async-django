from django.urls import path, include
from . import views

app_name = "blog_api"

urlpatterns = [
    path('sync', views.BlogView.as_view(), name='blog_view_sync'),
    path('async', views.BlogAsyncView.as_view(), name='blog_view_async'),
    path('heavy/<int:request_time>/', views.BlogAsyncParamView.as_view(), name='blog_view_async_with_param'),
]