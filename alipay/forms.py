# -*- coding:utf-8 -*-

from django import forms
from django.utils.safestring import mark_safe

from alipay import conf 
from alipay.widgets import ValueHiddenInput
from alipay.helpers import make_sign, get_form_data, urldecode


class AliPayPaymentBaseForm(forms.Form):
    """
    request interface. POST method, HTTPS
    """
        # base parameters
    service = forms.CharField(widget=ValueHiddenInput(), initial=conf.SERVICE[0])
    partner = forms.CharField(widget=ValueHiddenInput(), max_length=16, initial=conf.PARTNER)
    # 商户网站使用的编码格式，如utf-8、gbk、gb2312等 
    _input_charset = forms.CharField(widget=ValueHiddenInput(), initial='utf-8')
    # DSA、RSA、MD5三个值可选，必须大写  
    sign_type = forms.CharField(widget=ValueHiddenInput(), initial='MD5')
    sign = forms.CharField(widget=ValueHiddenInput())
    notify_url = forms.CharField(widget=ValueHiddenInput())
    return_url = forms.CharField(widget=ValueHiddenInput())
        # 需开通
    error_notify_url = forms.CharField(widget=ValueHiddenInput())
        # business parameters 
    out_trade_no = forms.CharField(widget=ValueHiddenInput(), max_length=64)
    subject = forms.CharField(widget=ValueHiddenInput(), max_length=256)
    payment_type = forms.CharField(widget=ValueHiddenInput(), initial=conf.PAYMENT_TYPE[0])
        # 买家 卖家 信息
    seller_id = forms.CharField(widget=ValueHiddenInput(), max_length=32, initial=conf.SELLER_ID)
    buyer_id = forms.CharField(widget=ValueHiddenInput(), max_length=32)
    seller_account_name = forms.CharField(widget=ValueHiddenInput(), max_length=100)
    buyer_account_name = forms.CharField(widget=ValueHiddenInput(), max_length=100)
    seller_email = forms.CharField(widget=ValueHiddenInput(), max_length=100)
    buyer_email = forms.CharField(widget=ValueHiddenInput(), max_length=100)
        # 买家逾期不付款，自动关闭交易 
    it_b_pay = forms.CharField(widget=ValueHiddenInput())
        # 价格 unit: RMB 
    price = forms.FloatField(widget=ValueHiddenInput(), min_value=0.01, max_value=1000000.00)
    quantity = forms.IntegerField(widget=ValueHiddenInput())
        # 担保交易不支持 total_fee
    total_fee = forms.FloatField(widget=ValueHiddenInput(), min_value=0.01, max_value=1000000.00)
    body = forms.CharField(widget=ValueHiddenInput(), max_length=1000)
    show_url = forms.CharField(widget=ValueHiddenInput(), max_length=400)
    paymethod = forms.CharField(widget=ValueHiddenInput(), initial=conf.PAYMETHOD[1])
    discount = forms.FloatField(widget=ValueHiddenInput())
        # CTU 支付宝风险稽查系统，需开通
    need_ctu_check = forms.CharField(widget=ValueHiddenInput())  # Y/N
    royalty_type = forms.CharField(widget=ValueHiddenInput(), max_length=2)  # 10
    royalty_parameters = forms.CharField(widget=ValueHiddenInput())
        # 需开通
    anti_phishing_key = forms.CharField(widget=ValueHiddenInput())
        # 需开通
    exter_invoke_ip = forms.CharField(widget=ValueHiddenInput(), max_length=15)
    extra_common_param = forms.CharField(widget=ValueHiddenInput(), max_length=100)
    extend_param = forms.CharField(widget=ValueHiddenInput())
    default_login = forms.CharField(widget=ValueHiddenInput())   # Y/N
    product_type = forms.CharField(widget=ValueHiddenInput(), max_length=50)
        # 需开通快捷登录
    token = forms.CharField(widget=ValueHiddenInput(), max_length=40)
    
    def get_action(self):
        return '%s?_input_charset=%s'% (conf.ALIPAY_GATEWAY, self['_input_charset'].value())


class AliPayBaseForm(forms.ModelForm):
    """
    Some models field
    """
    notify_time = forms.DateTimeField(input_formats=conf.ALIPAY_DATE_FORMAT)
    gmt_create = forms.DateTimeField(required=False, input_formats=conf.ALIPAY_DATE_FORMAT)
    gmt_payment = forms.DateTimeField(required=False, input_formats=conf.ALIPAY_DATE_FORMAT)
    gmt_close = forms.DateTimeField(required=False, input_formats=conf.ALIPAY_DATE_FORMAT)
    gmt_refund = forms.DateTimeField(required=False, input_formats=conf.ALIPAY_DATE_FORMAT)
    gmt_logistics_modify = forms.DateTimeField(required=False, input_formats=conf.ALIPAY_DATE_FORMAT)

    def clean_sign(self):
        data = get_form_data(self)
        sign = make_sign(data)
        if sign != data.get('sign'):
            self._errors['sign'] = self.error_class(['sign error!'])
        return sign


