from django.shortcuts import render

def home(request):
    return render(request, 'home/recipes_home.html')