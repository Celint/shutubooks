from django.db import models

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