import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dg_proj.settings')
import django
django.setup()

from api import models

# 一对一
author = models.Author.objects.filter(pk=1).first() # types:models.Author
# 正向查询： 对象.字段名
print(author)
# 反向查询: 对象.小写类名.字段名 或者 指定反向查询的字段 related_name
# print(author.authordetail.mobile)
print(author.detail.mobile)
# author.delete()

author_detail = models.AuthorDetail.objects.first()
print(author_detail.mobile)
print(author_detail.author.name)

# 一对多
publish = models.Publish.objects.filter(pk=1).first()
print(publish.name)
print(publish.books.filter(pk=1).first())

book = models.Book.objects.filter(pk=1).first()
print(book.name)
print(book.publish.name)

# 多对多
author = models.Author.objects.filter(pk=1).first()
print(author.name)
print(author.books.first().name)

book = models.Book.objects.filter(pk=1).first()
print(book.name)
print(book.authors.first())