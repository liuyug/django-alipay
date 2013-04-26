# -*- coding:utf-8 -*-

from django import forms

from alipay import conf
from alipay.widgets import ValueHiddenInput

class AliPaySendGoodsForm(forms.Form):
    """
    AliPay Send Goods confirm by platform
    """
        # base parameters
    service = forms.CharField(widget=ValueHiddenInput(), initial=conf.SERVICE[2])
    partner = forms.CharField(widget=ValueHiddenInput(), max_length=16, initial=conf.PARTNER)
    # 商户网站使用的编码格式，如utf-8、gbk、gb2312等 
    _input_charset = forms.CharField(widget=ValueHiddenInput(), initial='utf-8')
    # DSA、RSA、MD5三个值可选，必须大写  
    sign_type = forms.CharField(widget=ValueHiddenInput(), initial='MD5')
    sign = forms.CharField(widget=ValueHiddenInput())

    trade_no = forms.CharField(widget=ValueHiddenInput(), max_length=64)
        # 担保交易 物流
    logistics_name = forms.CharField(widget=ValueHiddenInput(), max_length=64)
    invoice_no = forms.CharField(widget=ValueHiddenInput(), max_length=32)
    transport_type = forms.CharField(widget=ValueHiddenInput(), max_length=32)
    create_transport_type = forms.CharField(widget=ValueHiddenInput(), max_length=32)
    seller_ip = forms.CharField(widget=ValueHiddenInput(), max_length=15)

    def get_action(self):
        return '%s?_input_charset=%s'% (conf.ALIPAY_GATEWAY, self['_input_charset'].value())


