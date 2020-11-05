from django.db import models


# 作品名称和作者(主演)
class Douban(models.Model):
    # id 自动创建
    comments = models.CharField(max_length=500)
    stars = models.IntegerField()
# Create your models here.
