from django.shortcuts import render

# Create your views here.


def main_page(request):
    a = '故宫'
    print(request)

    return render(request, 'test.html', {'abc':a,'a':"圆明园"})


