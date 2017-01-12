# -*- coding:utf-8 -*-

from django import forms

from .. import conf
from ..forms import AliPayPaymentBaseForm
from ..widgets import ValueHiddenInput


class AliPayPartnerTradeForm(AliPayPaymentBaseForm):
    """
    AliPay Partner Trade Form
    """
    service = forms.CharField(widget=ValueHiddenInput(), initial=conf.SERVICE[1])
        # 担保交易 物流
    logistics_type = forms.CharField(widget=ValueHiddenInput(), initial=conf.LOGISTICS_TYPE[0])
    logistics_fee = forms.CharField(widget=ValueHiddenInput(), initial='0.00')
    logistics_payment = forms.CharField(widget=ValueHiddenInput(), initial=conf.LOGISTICS_PAYMENT[0])
    logistics_type_1 = forms.CharField(widget=ValueHiddenInput())
    logistics_fee_1 = forms.CharField(widget=ValueHiddenInput())
    logistics_payment_1 = forms.CharField(widget=ValueHiddenInput())
    logistics_type_2 = forms.CharField(widget=ValueHiddenInput())
    logistics_fee_2 = forms.CharField(widget=ValueHiddenInput())
    logistics_payment_2 = forms.CharField(widget=ValueHiddenInput())
        # 卖家逾期不发货，允许买家退款
    t_s_send_1 = forms.CharField(widget=ValueHiddenInput())
        # 卖家逾期不发货，建议买家退款
    t_s_send_2 = forms.CharField(widget=ValueHiddenInput())
        # 买家逾期不确认收货，自动完成交易
    t_b_rec_post = forms.CharField(widget=ValueHiddenInput())
    receive_name = forms.CharField(widget=ValueHiddenInput(), max_length=128)
    receive_address = forms.CharField(widget=ValueHiddenInput(), max_length=256)
    receive_zip = forms.CharField(widget=ValueHiddenInput(), max_length=20)
    receive_phone = forms.CharField(widget=ValueHiddenInput(), max_length=30)
    receive_mobile = forms.CharField(widget=ValueHiddenInput())
