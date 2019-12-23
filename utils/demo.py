from django.http import HttpResponse


def index(request):

    print(123)
    return HttpResponse()


def demo(request):

    print("我是在dev新增的demo视图")
    print("123")

    return HttpResponse()