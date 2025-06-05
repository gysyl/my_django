from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=64, verbose_name="密码")
    age = models.IntegerField(verbose_name="年龄", blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="邮箱", blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name="手机号", blank=True, null=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"

    def __str__(self):
        return f"username:{self.username} (age: {self.age}, email: {self.email}, phone: {self.phone})"

class Department(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name="部门名称")
    location = models.CharField(max_length=64, verbose_name="部门位置", blank=True, null=True)

    class Meta:
        verbose_name = "部门信息"
        verbose_name_plural = "部门信息"

    def __str__(self):
        return f"title:{self.title} (location: {self.location})"