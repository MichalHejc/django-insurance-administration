from django.shortcuts import render

def index(request):
    return render(request, "clients/index.html")