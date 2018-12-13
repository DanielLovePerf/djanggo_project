# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserMessage(models.Model):
    # 设置最大长度，verbose_name在后台显示字段会用到
    object_id = models.CharField(primary_key=True, max_length=50,default="", verbose_name="主键")
    name = models.CharField(max_length=20, verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name="地址")
    message = models.CharField(max_length=500, verbose_name="留言信息")

    class Meta:
        verbose_name = u"用户留言信息"
        # db_table = "user_meassage" ，不自动生成表，指定表名字
        # ordering = '-object_id'  排序