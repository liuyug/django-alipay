# -*- coding:utf-8 -*-

import urllib2

from django.db import models
from alipay import conf
from alipay.models import AliPayBaseModel

from alipay.create_direct_pay_by_user.dpn.signals import alipay_dpn_flagged, alipay_dpn_successful

class AliPayDPN(AliPayBaseModel):
    """
    AliPay DPN 
    """
    gmt_close = models.DateTimeField(blank=True, null=True)
    extra_common_param = models.CharField(blank=True, null=True, max_length=256)
    out_channel_type = models.CharField(blank=True, null=True, max_length=256)
    out_channel_amount = models.CharField(blank=True, null=True, max_length=256)
    out_channel_inst = models.CharField(blank=True, null=True, max_length=256)

    class Meta:
        db_table = 'alipay_dpn'
        verbose_name = 'AliPay DPN'

    def send_signals(self):
        if self.notify_type != 'trade_status_sync':
            return
        if self.is_transaction():
            if self.flag:
                alipay_dpn_flagged.send(sender=self)
            else:
                alipay_dpn_successful.send(sender=self)

