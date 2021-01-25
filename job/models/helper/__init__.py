"""
公用的 class
"""

from django.db.models import Model, DateTimeField


class BaseModel(Model):
    create_at = DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    modify_at = DateTimeField(
        auto_now=True,
        verbose_name='更新时间'
    )

    class Meta:
        abstract = True


class BaseHistoricalRecords:
    """ 历史记录 model """

    def history_save(self, change_reason='@@'):
        """保存记录。
        1. 先调用一次 history_save()，不填写 change_reason，让之前的数据保存。
        2. 在调用一次 history_save(change_reason='xxx')， 将修改后的数据保存一次"""
        self.changeReason = change_reason
        self.save()
