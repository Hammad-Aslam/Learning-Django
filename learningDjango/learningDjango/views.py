from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, this is home.")
    return render(request, "home/index.html")


def about(request):
    # return HttpResponse("this is about.")
    return render(request, "about/index.html")


def faqs(request):
    # return HttpResponse("this is faqs.")
    return render(request, "faqs/index.html")
