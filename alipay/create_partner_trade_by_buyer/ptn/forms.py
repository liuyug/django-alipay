# -*- coding:utf-8 -*-

from django import forms

from alipay.helpers import make_sign
from alipay.create_partner_trade_by_buyer.ptn.models import AliPayPTN
from alipay.forms import AliPayBaseForm

class AliPayPTNForm(AliPayBaseForm):
    """
    AliPay Partner Trade Notify Form
    """
    class Meta:
        model = AliPayPTN
        fields = '__all__'

