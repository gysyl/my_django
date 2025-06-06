# Generated by Django 5.2.1 on 2025-06-07 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='书名')),
                ('author', models.CharField(blank=True, max_length=100, verbose_name='作者')),
                ('description', models.TextField(blank=True, verbose_name='简介')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='封面')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='分类名称')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='标签名称')),
            ],
        ),
        migrations.CreateModel(
            name='BookFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='books/')),
                ('file_format', models.CharField(choices=[('pdf', 'PDF'), ('epub', 'EPUB'), ('mobi', 'MOBI'), ('azw3', 'AZW3'), ('txt', 'TXT'), ('other', '其他')], max_length=10, verbose_name='文件格式')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='books.book', verbose_name='所属书籍')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, to='books.tag', verbose_name='标签'),
        ),
    ]
