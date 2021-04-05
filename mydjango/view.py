from django.shortcuts import render,HttpResponse
from .sam.getAddr import get_position
import json



def mainWindow(request):
    url = "<a href='http://127.0.0.1:8000/login/'>点击跳转</a>"
    context = dict()
    context['hello'] = 'Hello World!'
    context["url"] = url

    return render(request, "hello.html", context)



def travelHome(request):
    return render(request,"index.html")


def getArgx(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print (data)
        # TODO 处理函数
        pos = get_position(data["name"])

        result = {
            'pos':pos
        }
        return HttpResponse(json.dumps(result), content_type="application/json")
    else:
        return HttpResponse('Error')

def about(request):
    return render(request,"about.html")

def gallery(request):
    return render(request,"gallery.html")

def icons(request):
    return render(request,"icons.html")

def error404(request):
    return render(request,"404.html")

def blog(request):
    return render(request,"blog.html")

def blog_single(request):
    return render(request,"blog-single.html")

def contact(request):
    return render(request,"contact.html")

def select(request):
    return render(request,"select.html")