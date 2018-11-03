from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    zh = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    pub_date = models.DateField(default=timezone.now)
    yue = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    # def __str__(self):
    #     return ('账号：%s, 姓名：%s, 密码：%s, 密保：%s, 答案：%s, 注册时间：%s, 账户余额：%s') % (self.zh, self.name, self.password, self.question, self.answer, self.pub_date, self.yue)

