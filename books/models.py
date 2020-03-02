from django.db import models
# from account.models import stuInf
# Create your models here.


# class bookInf(models.Model):
#     owner = models.ForeignKey(stuInf, on_delete=models.CASCADE)  # 外键，外不了啊
#     # bookNum = models.AutoField(primary_key=True)#为什么要定义一个主键呢？我觉着可以不用了
#     bookName = models.CharField(max_length=30)  # 书名
#     type = models.CharField(max_length=20)  # 书籍标签
#     price = models.IntegerField(default=0)  # 价格
#     wearDegree = models.CharField(max_length=10, null=False)  # 新旧程度应该是
#     img = models.ImageField(upload_to='icons')  # 上传一张图片

#     class Meta:
#         verbose_name = '书籍信息'
