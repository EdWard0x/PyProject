from django.shortcuts import render,redirect

from site0219.utils.spider_animate import new_ani_time
from site0219.utils.forms import NewAniModelForm
from site0219 import models


def content(request):
    return redirect(to='/index/')


def main(request):
    rank_num = models.Ranking.objects.all().count()
    newani_num = models.NewAni.objects.all().count()
    nums = {
        'rank_num':rank_num,
        'newani_num':newani_num
    }
    return render(request, 'index.html',nums)