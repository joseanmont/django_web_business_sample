from django.shortcuts import render, HttpResponse

def about(request):
    return render(request, "core/about.html")

def home(request):
    return render(request, "core/home.html")

def store(request):
    return render(request, "core/store.html")