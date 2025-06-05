from django.db import models

# Create your models here.

class MyUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=256)  # 加密后存储
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

