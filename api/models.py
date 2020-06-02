from django.db import models
from utils.model import BaseModel


# Create your models here.
"""
Book表(name、price、img、authors、publish、is_delete、create_time)

Publish表(name、address、is_delete、create_time)

Author表(name、age、is_delete、create_time)

AuthorDetail表(mobile, author、is_delete、create_time)	

BaseModel基表(is_delete、create_time)
上面四表继承基表，可以继承两个字段
"""


class Book(BaseModel):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to='img', default='img/default.png')
    publish = models.ForeignKey(to='Publish', null=True, related_name='books',    db_constraint=False, on_delete=models.DO_NOTHING)
    authors = models.ManyToManyField(to='author', null=True, related_name='books', db_constraint=False)

    class Meta:
        # 表名称：
        db_table = 'old_boy_book'
        # 对象的一个易于理解的名称，为单数：在后台显示对对应的名称
        verbose_name = '书籍'
        # 该对象复数形式的名称：
        verbose_name_plural = verbose_name

    # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):
        return self.name


class Publish(BaseModel):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    class Meta:
        db_table = 'old_boy_publish'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=6)
    age = models.IntegerField()

    class Meta:
        db_table = 'old_boy_author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AuthorDetail(BaseModel):
    mobile = models.CharField(max_length=11)
    # db_constraint断开表关联，on_delete规定逻辑关联删除动作，models.CASCADE级联删除
    author = models.OneToOneField(to='author', null=True,
    db_constraint=False, on_delete=models.CASCADE, related_name='detail')

    class Meta:
        db_table = 'old_boy_author_detial'
        verbose_name = '作者详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s的详情' % self.author.name