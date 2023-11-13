from django.urls import path

from . import views

urlpatterns = [
    path('website_development', views.webdev, name='webdev'),
]