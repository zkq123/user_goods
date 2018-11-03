from django.db import models
from polls.models import User
from django.utils import timezone

class GoodsSort(models.Model):
    sort_name = models.CharField(max_length=50)
    sort_shortcut = models.CharField(max_length=20)

class Goods(models.Model):
    goods_bh = models.CharField(max_length=100, unique=True)
    goods_name = models.CharField(max_length=200)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_sort = models.CharField(max_length=20)
    sum = models.IntegerField(default=0)
    publish_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'users'

class GoodsChange(models.Model):
    change_name = models.CharField(max_length=50)
    change_bh = models.CharField(max_length=50)
    modify_date = models.DateTimeField(default=timezone.now)
    change_content = models.CharField(max_length=100)
    change_sum = models.IntegerField(default=0)
    change_sort = models.CharField(max_length=50,default='')

