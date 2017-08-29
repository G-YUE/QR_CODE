from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=32,verbose_name="用户名")
    password=models.CharField(max_length=64,verbose_name="密码")
    head=models.ImageField(verbose_name="头像",upload_to="static/image/")

class Erweima(models.Model):
    req=models.CharField(max_length=32,verbose_name="二维码唯一标识")
    choice=[(0,0),(1,1)]
    status=models.IntegerField(choices=choice,verbose_name="状态",default=0)
    ctime=models.IntegerField(default=100,verbose_name="超时时间")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

class Login(models.Model):
    user=models.ForeignKey("User")
    erweima=models.ForeignKey("Erweima")