from django.db import models


class NewAni(models.Model):
    title = models.CharField(verbose_name='番名', max_length=32)
    date = models.CharField(verbose_name='日期', max_length=8)
    day_of_week = models.IntegerField(verbose_name='星期')
    pub_index = models.CharField(verbose_name='更新集数', max_length=16)
    pub_time = models.CharField(verbose_name='更新时间', max_length=8)
    season_id = models.IntegerField(verbose_name='seasonid')
    cover = models.ImageField(verbose_name='cover')
    ep_cover = models.ImageField(verbose_name='epcover')
    square_cover = models.ImageField(verbose_name='squarecover')
    episode_id = models.IntegerField(verbose_name='episode_id', null=True, blank=True)
    vedio_addr = models.CharField(verbose_name='播放地址', max_length=256, null=True, blank=True)


class Ranking(models.Model):
    title = models.CharField(verbose_name='番名', max_length=32)
    viewers = models.CharField(verbose_name='观众数', max_length=16)
    likers = models.CharField(verbose_name='收藏数', max_length=16)
    addr = models.CharField(verbose_name='播放地址', max_length=256)


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username
