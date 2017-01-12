# -*- coding:utf-8 -*-

from django import forms

from .models import AliPayPTN
from ...forms import AliPayBaseForm


class AliPayPTNForm(AliPayBaseForm):
    """
    AliPay Partner Trade Notify Form
    """
    class Meta:
        model = AliPayPTN
        fields = '__all__'
