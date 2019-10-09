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
    bookNum = models.CharField(max_length=10,primary_key=True)
    bookName = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    wearDegree = models.CharField(max_length=10, null=False)

    class Meta:
        verbose_name = 'bookInf'

# class imgInf(models.Model):
#     imgNum = models.CharField(max_length=10, primary_key=True)
#     bookNum = models.ForeignKey('bookInf',on_delete=models.CASCADE)
#     img = models.ImageField()

class recordInf(models.Model):
    ownNum = models.ForeignKey('stuInf',on_delete=models.CASCADE,primary_key=True)
    buyNum = models.ForeignKey('stuInf',on_delete=models.CASCADE,primary_key=True)
    bookNum = models.ForeignKey('bookInf',on_delete=models.CASCADE,primary_key=True)
    # imgNum = models.ForeignKey('imgInf',on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True,primary_key=True)
