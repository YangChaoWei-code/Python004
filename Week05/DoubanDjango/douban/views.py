from django.shortcuts import render
from .models import Douban

def index(request):
    ###  从models取数据传给template  ###
    shorts = Douban.objects.all()
    # 评论数量
    plus = Douban.objects.filter(stars__gt=3)

    return render(request, 'index.html', locals())

# 通过搜索框的关键字展示相关短评内容
def search(request):
    keyword = request.GET['q']  # 搜索的关键字
    search_comment = Douban.objects.filter(comments__contains=keyword)  # 关键字相关的短评内容
    return render(request, 'comments.html', locals())
# Create your views here.
