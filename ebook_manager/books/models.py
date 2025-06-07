
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# 自定义用户管理器（可选，用于创建用户）
class ReaderManager(BaseUserManager):
    def create_user(self, username, password=None, email=None):
        if not username:
            raise ValueError("用户必须有用户名")
        user = self.model(username=username, email=email)
        user.set_password(password)  # 自动哈希密码
        user.save(using=self._db)
        return user

class Reader(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码")
    email = models.EmailField(blank=True, null=True, verbose_name="邮箱")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="最后登录时间")
    is_active = models.BooleanField(default=True, verbose_name="是否活跃")

    # 显式定义groups和user_permissions，设置唯一的related_name
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='用户组',
        blank=True,
        help_text='该用户所属的用户组',
        related_name='reader_groups',  # 关键修改：唯一名称，避免与auth.User冲突
        related_query_name='reader'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='用户权限',
        blank=True,
        help_text='该用户拥有的直接权限',
        related_name='reader_user_permissions',  # 关键修改：唯一名称
        related_query_name='reader'
    )

    objects = ReaderManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "读者"
        verbose_name_plural = "读者"

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="分类名称")
    slug = models.SlugField(max_length=70, unique=True, blank=True, verbose_name="URL标识")  # 新增

    class Meta:
        verbose_name = "书籍分类"
        verbose_name_plural = "书籍分类"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="标签名称")
    slug = models.SlugField(max_length=40, unique=True, blank=True, verbose_name="URL标识")  # 新增

    class Meta:
        verbose_name = "书籍标签"
        verbose_name_plural = "书籍标签"

    def __str__(self):
        return self.name

# 自动生成slug（保存前触发）
@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=Tag)
def auto_generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name, allow_unicode=True)  # 支持中文slug

import os
from django.utils import timezone

def cover_upload_path(instance, filename):
    # 动态路径：covers/用户ID/年/月/文件名（避免文件冲突）
    return f"covers/user_{instance.reader.id if instance.reader else '0'}/{timezone.now().strftime('%Y/%m')}/{filename}"

def book_file_upload_path(instance, filename):
    # 动态路径：books/书籍ID/年/月/文件名
    return f"books/book_{instance.book.id}/{timezone.now().strftime('%Y/%m')}/{filename}"

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="书名")
    author = models.CharField(max_length=100, blank=True, verbose_name="作者")
    description = models.TextField(blank=True, verbose_name="简介")
    cover = models.ImageField(upload_to=cover_upload_path, blank=True, null=True, verbose_name="封面")  # 动态路径
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="分类")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="标签")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    reader = models.ForeignKey('Reader', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="上传者")
    view_count = models.PositiveIntegerField(default=0, verbose_name="浏览量")  # 新增统计字段

    class Meta:
        verbose_name = "电子书"
        verbose_name_plural = "电子书"
        ordering = ["-created_at"]  # 默认按添加时间倒序排列

    def __str__(self):
        return f"{self.title}（作者：{self.author or '未知'}）"  # 显示作者信息

class BookFile(models.Model):
    FORMAT_CHOICES = [
        ("pdf", "PDF"),
        ("epub", "EPUB"),
        ("mobi", "MOBI"),
        ("azw3", "AZW3"),
        ("txt", "TXT"),
        ("other", "其他"),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="files", verbose_name="所属书籍")
    file = models.FileField(upload_to=book_file_upload_path, verbose_name="文件路径")  # 动态路径
    file_format = models.CharField(max_length=10, choices=FORMAT_CHOICES, verbose_name="文件格式")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
    file_size = models.PositiveIntegerField(blank=True, null=True, verbose_name="文件大小（字节）")  # 新增字段
    download_count = models.PositiveIntegerField(default=0, verbose_name="下载次数")  # 新增统计字段

    class Meta:
        verbose_name = "电子书文件"
        verbose_name_plural = "电子书文件"

    def save(self, *args, **kwargs):
        # 自动记录文件大小（需在保存前获取）
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} - {self.get_file_format_display()}（{self.file_size|filesizeformat}）"  # 显示文件大小

class DownloadRecord(models.Model):
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE, verbose_name="下载者")
    book_file = models.ForeignKey('BookFile', on_delete=models.CASCADE, verbose_name="下载的文件")
    downloaded_at = models.DateTimeField(auto_now_add=True, verbose_name="下载时间")
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name="下载IP")  # 新增
    user_agent = models.CharField(max_length=512, blank=True, null=True, verbose_name="用户代理")  # 新增

    class Meta:
        verbose_name = "下载记录"
        verbose_name_plural = "下载记录"
        ordering = ["-downloaded_at"]  # 按时间倒序排列

    def __str__(self):
        return f"{self.reader.username} 下载了 {self.book_file.book.title}（{self.book_file.get_file_format_display()}）"