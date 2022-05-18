from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from myapp.models import *


def show_about_page(request):
    name = "Hanuman"
    email = "hanu@hanuman.com"
    data_dict = {"name": name, "email": email}
    return render(request, "about.html", data_dict)


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {"images": images, "cats": cats}
    return render(request, "home.html", data)


def show_category_page(request, cid):
    category = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=category)
    cats = Category.objects.all()
    data = {"images": images, "cats": cats}
    return render(request, "home.html", data)


def home(request):
    return redirect("/home")


def show_search_page(request):
    searched_query = request.GET["search"]
    if searched_query:
        result = Image.objects.filter(title__contains=searched_query)
    else:
        result = None
    cats = Category.objects.all()
    data = {"images": result, "cats": cats}
    return render(request, "home.html", data)
