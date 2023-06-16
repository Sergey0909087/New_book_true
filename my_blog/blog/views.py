from django.shortcuts import render, redirect

def yandex(request):
    return render(request, 'blog/yandex.html')

# Create your views here.
