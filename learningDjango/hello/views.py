from django.shortcuts import render

# Create your views here.


def hello_jinja(request):
    return render(request, "hello/hello.html")
