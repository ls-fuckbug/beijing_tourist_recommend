from django.shortcuts import render,HttpResponse
import json
import urllib.parse
from .sam.main_pro import *




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
        # 解析参数
        raw_data = urllib.parse.unquote(str(request.body,'utf-8'))
        spot_data = raw_data.split('&')
        spot_num = spot_data.pop().lstrip('num=')
        # 错误处理
        if spot_num == "输入景点个数":
            return render(request, "404.html")

        # 取出目标景点个数
        num = int(spot_num)
        print(num)
        # 取出选择的景点
        spot_list = [s.lstrip('spot=') for s in spot_data]
        print(spot_list)
        # 错误处理
        if len(spot_list) == 0:
            return render(request, "404.html")

        # 推荐路线
        route_list = tra_rec(spot_list,num)
        print(route_list)
        # 传给前端
        route = dict()

        route['spot_name'] = route_list[0]

    return render(request,"route.html",route)