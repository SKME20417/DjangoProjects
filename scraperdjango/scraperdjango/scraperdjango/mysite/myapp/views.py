from django.shortcuts import render
import requests
import bs4
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect


# Create your views here.
def scrap(request):
    if request.method == "POST":
        site = request.POST.get('site', '')
        response = requests.get(site)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")

        for link in links:
            linkaddress = link.get("href")
            linktext = link.string
            Link.objects.create(address = linkaddress, name = linktext)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
    return render(request, "myapp/result.html", {'data':data})

def delete(request):
    links = Link.objects.all()
    links.delete()
    return render(request, "myapp/result.html" )