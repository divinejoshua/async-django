from django.urls import path, include
from . import views

app_name = "blog_api"

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog_view'),                       #Check user api
]