# coding=utf-8
# 全局上下文
from django.db.models import Count
from post.models import Post


def getRightInfo(request):
    # 获取分类信息
    r_catepost = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')
    # A = Post.objects.values('category__cname', 'category').annotate(c=Count('*'))
    # B = Post.objects.values('category__cname', 'category')
    # C = Post.objects.all()
    # D = Post.objects.values('category__cname', 'category').annotate
    # print(A)
    # print(B)
    # print(C)
    # print(D)

    # 近期文章
    r_recpost = Post.objects.all().order_by('-created')[:3]

    # 获取归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT created,count('*') from t_post GROUP BY DATE_FORMAT(created,'%Y-%m');")
    r_filepost = cursor.fetchall()

    return {'r_catepost': r_catepost,'r_recpost':r_recpost,'r_filepost':r_filepost}
