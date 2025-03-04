from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogview, name="blogview"),
 
]