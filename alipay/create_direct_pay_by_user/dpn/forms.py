# -*- coding:utf-8 -*-

from django import forms

from .models import AliPayDPN
from ...forms import AliPayBaseForm


class AliPayDPNForm(AliPayBaseForm):
    """
    AliPay Direct Payment Notify Form
    """
    class Meta:
        model = AliPayDPN
        fields = '__all__'
