from django.shortcuts import render
from django.http import HttpResponse
from . models import User
from goods.models import GoodsSort, Goods, GoodsChange
from django.db.models import F
import datetime,time
import random
import math
def index(request):
    return render(request, 'polls/index.html')

def vote(request):
    return render(request, 'polls/detail.html')

def detail(request):
    n = User.objects.create(zh=request.POST['user_zh'], name=request.POST['user_name'], password=request.POST['user_password'], question=request.POST['user_question'], answer=request.POST['user_answer'])
    n.save()
    return render(request, 'polls/result.html', {'user':n})

def denglu(request):
        a = User.objects.filter(zh=request.POST['user_zh']).filter(password=request.POST['user_password']).exists()
        if a:
            user = User.objects.get(zh=request.POST['user_zh'])
            return render(request, 'polls/result.html', {'user':user})
        else:
            return render(request, 'polls/register.html')


def message(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'polls/message.html', {'user':user})

def message_2(request, user_id):
    user = User.objects.get(pk=user_id)
    return  render(request, 'polls/message_2.html', {'user':user})

def message_2_1(request, user_id):
    User.objects.filter(pk=user_id).update(yue=F('yue') + request.POST['user_yue'])
    user = User.objects.get(pk=user_id)
    return render(request, 'polls/result.html',{'user':user})

def message_3(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'polls/result.html', {'user':user})

def message_4(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'polls/message_4.html', {'user':user})

def message_4_1(request, user_id):
    a = User.objects.get(pk=user_id)
    if a.password == request.POST['user_password']:
        a.password = request.POST['password_1']
        a.save()
        return render(request, 'polls/result.html', {'user':a})
    else:
        return render(request, 'polls/message_4.html',{'user':a})

def register(request):
    return render(request, 'polls/register.html')

def found(request):
    return render(request, 'polls/found.html')

def found_1(request):
    try:
        user = User.objects.get(zh=request.POST['user_zh'])
        print(user)
    except:
        return render(request, 'polls/found.html')
    else:
        return render(request, 'polls/found_2.html', {'user':user})

def found_2(request, user_id):
    user = User.objects.get(pk=user_id)
    if user.answer == request.POST['user_answer']:
        return render(request, 'polls/found_1.html', {'user':user})
    else:
        return render(request, 'polls/found_2.html', {'user':user})

def found_3(request, user_id):
    user = User.objects.get(pk=user_id)
    user.password = request.POST['user_pwd']
    user.save()
    return render(request, 'polls/index.html')

def look(request):
    return HttpResponse("暂时还没商品哦")

def add_goods(request,user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'polls/add_goods.html',{'user':user})

def save_goods(request,user_id):
    goods = Goods(goods_name=request.POST['good_name'], goods_price=request.POST['good_price'], goods_sort=request.POST['good_sort'], sum=request.POST['sum'])
    goods.goods_bh = goods.goods_sort + str(math.ceil(time.time())) + str(random.randint(0,9))*3
    user = User.objects.get(pk=user_id)
    goods.user=user
    goods.save()
    print(user.users.all())
    return render(request, 'polls/result.html', {'goods':goods,'user':user})

def check(request,user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'polls/check.html',{'user':user})

def change(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'polls/change.html', {'user':user})

def change_1(request, user_id):
    user = User.objects.get(pk=user_id)
    print(request.POST['goods_change'])
    goods = Goods.objects.get(pk=request.POST['goods_change'])
    print(goods)
    return render(request, 'polls/change_1.html', {'user':user, 'goods':goods})

def change_2(request, user_id, goods_bh):
    user = User.objects.get(pk=user_id)
    goods = Goods.objects.get(goods_bh=goods_bh)
    goods.goods_name = request.POST['good_name']
    goods.goods_price = request.POST['good_price']
    goods.goods_sort = request.POST['good_sort']
    goods.sum = request.POST['sum']
    goods.save()
    c = GoodsChange(change_name=request.POST['good_name'], change_bh =goods_bh, change_content = request.POST['good_price'], change_sum=request.POST['sum'], change_sort = request.POST['good_sort'])
    c.save()
    return render(request, 'polls/result.html', {'user':user, 'goods':goods})

def check_change(request, user_id):
    user = User.objects.get(pk=user_id)
    s = GoodsChange.objects.all()
    return render(request, 'polls/final.html',{'user':user, 's':s})