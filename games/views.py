

# 主页
from django.shortcuts import render


def hello(request):
    return render(request,"index.html")

# 登录
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method=="POST":
        pass

# 注册
def signup(request):
    pass

# 选择
def select(request):
    pass
