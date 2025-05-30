from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30, 
                                default='',
                                null=False,
                                unique=True,
                                verbose_name='书名')
    price = models.DecimalField(max_digits=7, decimal_places=2,
                                default=0.00,
                                null=False,
                                verbose_name='定价')
    
    pub_house = models.CharField(max_length=50,
                                    default='',
                                    null=False,
                                    verbose_name='出版社')
    market_price = models.DecimalField(max_digits=7, decimal_places=2,
                                    default=0.00,
                                    null=False,
                                    verbose_name='零售价')
    def __str__(self):
        return f"书名：{self.title} 价格：{self.price} 出版社：{self.pub_house} 零售价：{self.market_price}"
    
    class Meta:
        #db_table = 'mybook'
        #verbose_name = 'book'
        #verbose_name_plural = '图书'
        pass
    
    
class Author(models.Model):
    name = models.CharField(max_length=30,
                                default='',
                                null=False,
                                unique=True,
                                verbose_name='作者')
    age = models.IntegerField(default=1,
                                null=False,
                                verbose_name='年龄')
    email = models.EmailField(default='xxx@yyyy.zzz',
                                null=False,
                                verbose_name='邮箱')                    
    def __str__(self):
        return f"作者：{self.name} 年龄：{self.age} 邮箱：{self.email}"
    
class Wife(models.Model):
    name = models.CharField(max_length=30,
                                default='',
                                null=False,
                                unique=True,
                                verbose_name='妻子姓名')
    age = models.IntegerField(default=1,
                                null=False,
                                verbose_name='年龄')    
    author = models.OneToOneField(Author, on_delete=models.CASCADE, 
                                verbose_name='丈夫')   

    def __str__(self):
        return f"妻子：{self.name} 年龄：{self.age} 作者：{self.author.name}"