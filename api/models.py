from django.db import models
from

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


class Publish(BaseModel):
    name = models.CharField(max_length=6)
    address = models.CharField(max_length=6)


class Author(BaseModel):
    name = models.CharField(max_length=6)
    age = models.IntegerField()


class AuthorDetail(BaseModel):
    mobile = models.CharField(max_length=11)
