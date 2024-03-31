# from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse, HttpResponseRedirect


# def signin(request):
#     template = loader.get_template("login.html")
#     return HttpResponse(template.render({}, request))

# def index(request):
#     return render(request, 'login.html')


# def signup(request):
#     template = loader.get_template("makeaccounts.html")
#     return HttpResponse(template.render({}, request))




# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
# from .models import CustomUser
# from django.template import loader


# def index(request):
#     context = {'user': request.user}
#     return render(request, 'index.html', context)

# def signup(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     new_user = CustomUser(username=username, password=password)
#     new_user.save()
#     return HttpResponse('ユーザーの作成に成功しました')


# from django.contrib.auth import login

# def signin(request):
#     username = request.POST['username']
#     password = request.POST['password']

#     try:
#         user = CustomUser.objects.get(username=username)
#     except CustomUser.DoesNotExist:
#         return HttpResponse('ログインに失敗しました')

#     if user.password == password:
#         login(request, user)  # これを実行するとユーザをログイン状態にできる
#         return HttpResponseRedirect('/')
#     else:
#         return HttpResponse('ログインに失敗しました')
    
# def signout(request):
#     logout(request)
#     return HttpResponseRedirect('/')




from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login,logout

def signup(request):
    context = {'user': request.user}
    return render(request, 'signup.html', context)

def signin(request):
    context = {'user': request.user}
    return render(request, 'login.html', context)


def signupsent(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = CustomUser(username=username, password=password)
    new_user.save()
    return HttpResponse('ユーザーの作成に成功しました')


def signinsent(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponse('ログインに失敗しました')

    if user.password == password:
        login(request, user)  # これを実行するとユーザをログイン状態にできる
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('ログインに失敗しました')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/')