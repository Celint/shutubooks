from django.db import models


class stuInf(models.Model):
    stuNum = models.CharField(max_length=10,unique=True)  # 学号唯一
    stuName = models.CharField(max_length=30)  # 用户名
    stuPassWord = models.CharField(max_length=16)  # 密码
    stuCollege = models.CharField(max_length=30)  # 学校
    stuImg = models.ImageField(upload_to='icons/', default='icons/default_boy.png')
    def __str__(self):
        return self.stuName
    class Meta:
        verbose_name = 'User'
