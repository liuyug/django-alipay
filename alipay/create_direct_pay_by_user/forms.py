
from django import forms

from alipay import conf
from alipay.forms import AliPayPaymentBaseForm
from alipay.widgets import ValueHiddenInput

class AliPayDirectPayForm(AliPayPaymentBaseForm):
    """
    AliPay Direct Pay Form
    """
    service = forms.CharField(widget=ValueHiddenInput(), initial=conf.SERVICE[0])
    item_orders_info = forms.CharField(widget=ValueHiddenInput(), max_length=40000)
