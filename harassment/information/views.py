from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def aboutus(request):
    return render(request, "about.html")

def tellus(request):
    return render(request, "tellus.html")

def harassment(request):
    return render(request, "harassment.html")

def joinus(request):
    return render(request, "joinus.html")
