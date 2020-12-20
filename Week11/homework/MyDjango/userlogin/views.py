from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("Hello Django!")


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return render(request, 'result.html', locals())
            else:
                return HttpResponse('密码错误')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'user_form.html', {'form': login_form})

# Create your views here.
