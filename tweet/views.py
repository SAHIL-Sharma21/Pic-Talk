from django.shortcuts import render

# Create your views here.
#testing view

def index(request):
    return render(request, 'index.html')