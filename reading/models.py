from django.db import models
from account.models import stuInf
# Create your models here.
# '''账户的数据表'''
# class Accout(models.Model):
#     username = models.CharField(max_length=64, unique=True)
#     email = models.EmailField()
#     password = models.CharField(max_length=128)
#     sid = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.username
#
# '''文章的数据表'''
# class Article(models.Model):
#     title = models.CharField(max_length=255, unique=True)
#     content = models.TextField("文章内容")
#     account = models.ForeignKey("reading.Accout", verbose_name="作者", on_delete=models.CASCADE)
#     tags = models.ManyToManyField("Tag", blank=True)
#     public_date = models.DateTimeField()
#     read_count = models.IntegerField(default=0)
#
# '''文章标签'''
# class Tag(models.Model):
#     name = models.CharField(max_length=64, unique=True)

class article(models.Model):
    tittle = models.CharField(max_length=30)
    content = models.TextField("内容")  #用于存储文章主题内容，要存储的是HTML
    authur = models.ForeignKey(stuInf, verbose_name="作者", on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    read_count = models.IntegerField(default=0)
    as_draft = models.BooleanField(default=False)#是否存为草稿
class image(models.Model):#用于存储文章中的图片
    image = models.ImageField(upload_to='articles/')
    # article = models.ForeignKey(article, on_delete=models.CASCADE)

