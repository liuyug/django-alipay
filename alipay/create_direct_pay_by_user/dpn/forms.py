# -*- coding:utf-8 -*-

from django import forms

from alipay.create_direct_pay_by_user.dpn.models import AliPayDPN
from alipay.forms import AliPayBaseForm

class AliPayDPNForm(AliPayBaseForm):
    """
    AliPay Direct Payment Notify Form
    """
    class Meta:
        model = AliPayDPN
        fields = '__all__'

