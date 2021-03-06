import math

from django.shortcuts import render

# Create your views here.
# 渲染主页面
from post.models import Post
from django.core.paginator import Paginator


def queryAll(request, num=1):
    num = int(num)
    # 获取所有帖子信息(降序排列)
    postList = Post.objects.all().order_by('-created')
    # 创建分页器对象，每页只有一条帖子
    pageObj = Paginator(postList, 1)
    # 获取当前页的数据
    perPageList = pageObj.page(num)
    # 每页开始页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # 每页结束页码
    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    return render(request, 'index.html', {'postList': perPageList, 'pageList': pageList, 'currentNum': num})


# 阅读全文功能
def detail(request, postid):
    postid = int(postid)
    # 根据postid查询帖子的详情信息
    post = Post.objects.get(id=postid)
    return render(request, 'detail.html', {'post': post})


# 根据类别id查询所有帖子
def queryPostByCid(request, cid):
    postList = Post.objects.filter(category_id=cid)
    return render(request, 'article.html', {'postList': postList})


# 根据发帖时间查询所有帖子
def queryPostByCreated(request, year, month):
    postList = Post.objects.filter(created__year=year, created__month=month)
    return render(request, 'article.html', {'postList': postList})
