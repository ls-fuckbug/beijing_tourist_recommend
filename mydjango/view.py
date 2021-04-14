from django.shortcuts import render,HttpResponse
import json
import urllib.parse
from .sam.main_pro import *




# test
def mainWindow(request):
    url = "<a href='http://127.0.0.1:8000/login/'>点击跳转</a>"
    context = dict()
    context['hello'] = 'Hello World!'
    context["url"] = url
    return render(request, "hello.html", context)


def travelHome(request):
    return render(request,"index.html")


def spot_choose(request):
    return render(request,"spot.html")


def route_show(request):
    return render(request,"route.html")



def about(request):
    return render(request,"about.html")


def gallery(request):
    return render(request,"gallery.html")


def error404(request):
    return render(request,"404.html")


def blog(request):
    return render(request,"blog.html")


def blog_single(request):
    return render(request,"blog-single.html")


def contact(request):
    return render(request,"contact.html")


def reco(request):
    if request.method == "POST":
        raw_data = urllib.parse.unquote(str(request.body,'utf-8'))
        spot_data = raw_data.split('&')
        spot_list = [ s.lstrip('spot=') for s in spot_data]
        print(spot_list)
        route_list = tra_rec(spot_list,10)
        print(route_list)

        route = dict()
        route['spot_name'] = route_list[0]

    return render(request,"route.html",route)