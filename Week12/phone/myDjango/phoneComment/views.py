from django.shortcuts import render
from .models import PhoneComment
from django.shortcuts import render
from django.db.models import Avg, Count, Sum
from django.http.response import HttpResponse
from datetime import datetime, timedelta
# from .models import Comments Category

def index(request):
    ###  从models取数据传给template  ###
    shorts = PhoneComment.objects.all()
    all_products = shorts.values('product_name','description','price').distinct()
    # 评论数量
    counter = PhoneComment.objects.all().count()
    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {PhoneComment.objects.aggregate(Avg('price'))['price__avg']:0.1f} "
    # 情感倾向
    sent_avg =f" {PhoneComment.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = PhoneComment.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = PhoneComment.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())

# 通过搜索框的关键字展示相关短评内容
def search(request):
    keyword = request.GET['q']  # 搜索的关键字

    search_comment = PhoneComment.objects.filter(product_name__contains=keyword)  # 关键字相关的短评内容
    if search_comment:
        # 评论数量
        counter = search_comment.count()
        product = search_comment.values('product_name','description','price').distinct()
        # 平均星级
        # star_value = T1.objects.values('n_star')
        star_avg = f" {search_comment.aggregate(Avg('price'))['price__avg']:0.1f} "
        # 情感倾向
        sent_avg =f" {search_comment.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

        # 正向数量
        queryset = search_comment.values('sentiment')
        condtions = {'sentiment__gte': 0.5}
        plus = queryset.filter(**condtions).count()

        # 负向数量
        queryset = search_comment.values('sentiment')
        condtions = {'sentiment__lt': 0.5}
        minus = queryset.filter(**condtions).count()
    else:
        return render(request, 'noPhone.html', locals())
    return render(request, 'comments.html', locals())

