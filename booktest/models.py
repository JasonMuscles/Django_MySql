from django.db import models

# Create your models here.
class bookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    booktitle = models.CharField(max_length=20)

    # 出版日期
    book_publish_data = models.DateField()

    # 阅读量
    book_read = models.IntegerField(default=0)

    # 评论量
    book_comment = models.IntegerField(default=0)

    # 删除标记
    is_Delete = models.BooleanField(default=False)