from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeFiled(auto_now_add=True, null=True)
    is_delete = models.BooleanField(default=False)
    class Meta:
        # 抽象表，不会完成数据库迁移
        abstract = True
