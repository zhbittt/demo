from django.shortcuts import render, HttpResponse, redirect
from demo_app.models import UserInfo
from demo_app.form import LoginForm

# Create your views here.


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/demo/index')
        return render(request, 'login.html', {'form': form})
    return HttpResponse("hello world")


def index(request):
    return render(request, 'index.html')

