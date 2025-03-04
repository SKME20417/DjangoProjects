from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blogview(request):
    # return  HttpResponse("This is a new blog view and you are craeting a function here")
    return render(request, "blog/blog.html")