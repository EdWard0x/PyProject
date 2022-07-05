import re

from django.shortcuts import render

from site0219.utils.conversion import str2value
from site0219 import models
from site0219.utils.pagination import Pagination
from site0219.utils.spider_animate import new_ani_time, ani_ranking


def list(request):
    res_list = new_ani_time()
    models.NewAni.objects.all().delete()
    for obj in res_list:
        # print(obj)
        # if not models.NewAni.objects.filter(episode_id=obj['episode_id']):
        models.NewAni.objects.create(**obj)
    # form = NewAniModelForm()
    query = models.NewAni.objects.all()
    # print(query)
    data = {
        'query': query
    }
    return render(request, 'newani.html', data)


def rank(request):
    models.Ranking.objects.all().delete()
    res = ani_ranking()
    for obj in res:
        models.Ranking.objects.create(**obj)

    queryset = models.Ranking.objects.all()

    # 2.实例化分页对象
    page_object = Pagination(request, queryset)

    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'ranking.html', context)


def pie_chart(request):
    query = models.Ranking.objects.all()
    title = []
    i_list = []
    o_list = []
    inner_ring_list = []
    outer_ring_list = []
    tmp_out_list = []
    tmp_in_list = []

    '''获取query对象字段值并加入列表'''
    for i in query:
        title.append(i.title)
        outer_ring_list.append(i.viewers)
        inner_ring_list.append(i.likers)

    '''处理带有汉字的数值并转换成int'''
    for i in inner_ring_list:
        i_list.append(str2value(i))
    for i in outer_ring_list:
        o_list.append(str2value(i))

    for i, j in zip(title, o_list):
        dic = {
            'vvalue': j,
            'nname':i

        }
        tmp_out_list.append(dic)

    for i, j in zip(title, i_list):
        dic = {
            'vvalue': j,
            'nname': i

        }
        tmp_in_list.append(dic)

    data = {
        'query': query,
        # 'title': title,
        'tmp_out_list': tmp_out_list,
        'tmp_in_list':tmp_in_list
    }

    return render(request, 'piechart.html', data)



def histogram_chart(request):

    return render(request,'histogramchart.html')