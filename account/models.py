from django.db import models


class stuInf(models.Model):
    stuNum  = models.CharField(max_length=10, primary_key=True)
    stuName = models.CharField(max_length=30)
    stuPassWord = models.CharField(max_length=16)
    stuCollege = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'stuInf'

class bookInf(models.Model):
    ownerNum = models.ForeignKey('stuInf',on_delete=models.CASCADE)
    bookNum = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    wearDegree = models.CharField(max_length=10, null=False)
    img = models.ImageField(upload_to='icons')

    class Meta:
        verbose_name = 'bookInf'



class recordInf(models.Model):
    ownNum = models.ForeignKey('stuInf',on_delete=models.CASCADE,related_name='owner')
    buyNum = models.ForeignKey('stuInf',on_delete=models.CASCADE,related_name='buyer')
    bookNum = models.ForeignKey('bookInf',on_delete=models.CASCADE)
    # imgNum = models.ForeignKey('imgInf',on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'recordInf'
        unique_together = (("ownNum", "buyNum","bookNum","time"))