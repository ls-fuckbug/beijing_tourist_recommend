from django.shortcuts import render
from .sam.sam import getnum



def runoob(request):
    print(getnum(77777))
    url = "<a href='https://www.runoob.com/'>点击跳转</a>"
    context = {}
    context['hello'] = 'Hello World!'
    context["url"] = url

    return render(request, "hello.html", context)