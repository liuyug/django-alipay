# -*- coding:utf-8 -*-


from django.db import models

from ...models import AliPayBaseModel

from .signals import alipay_ptn_flagged, alipay_ptn_successful


class AliPayPTN(AliPayBaseModel):
    """
    AliPay PTN (partner trade)
    """
    # 担保交易
    logistics_type = models.CharField(blank=True, null=True, max_length=256)
    logistics_fee = models.CharField(blank=True, null=True, max_length=256)
    logistics_payment = models.CharField(blank=True, null=True, max_length=256)
    gmt_logistics_modify = models.DateTimeField(blank=True, null=True, max_length=256)
    buyer_actions = models.CharField(blank=True, null=True, max_length=256)
    seller_actions = models.CharField(blank=True, null=True, max_length=256)
    receive_name = models.CharField(blank=True, null=True, max_length=256)
    receive_address = models.CharField(blank=True, null=True, max_length=256)
    receive_zip = models.CharField(blank=True, null=True, max_length=256)
    receive_phone = models.CharField(blank=True, null=True, max_length=256)
    receive_mobile = models.CharField(blank=True, null=True, max_length=256)

    class Meta:
        db_table = 'alipay_ptn'
        verbose_name = 'AliPay PTN'

    def send_signals(self):
        if self.notify_type != 'trade_status_sync':
            return
        if self.is_transaction():
            if self.flag:
                alipay_ptn_flagged.send(sender=self)
            else:
                alipay_ptn_successful.send(sender=self)
