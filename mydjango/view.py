from django.shortcuts import render,HttpResponse
from .sam.sam import getnum
from .sam.getAddr import get_position
import json



def mainWindow(request):
    url = "<a href='http://127.0.0.1:8000/login/'>点击跳转</a>"
    context = dict()
    context['hello'] = 'Hello World!'
    context["url"] = url

    return render(request, "hello.html", context)


def loginWindow(request):
    return render(request,"login.html")


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