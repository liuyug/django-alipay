
import urllib2
import datetime
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.utils.http import urlencode

from alipay.create_direct_pay_by_user.dpn.signals import alipay_dpn_successful
from alipay.create_partner_trade_by_buyer.ptn.signals import alipay_ptn_successful, alipay_ptn_flagged

from alipay.send_goods_confirm_by_platform.forms import AliPaySendGoodsForm
from alipay.helpers import make_sign, get_form_data

def alipay_send_goods(trade_obj):
    """Send Goods to buyer"""
    sign_type = 'MD5'
    site = Site.objects.get_current()
    alipay_dict = {
            'sign_type': sign_type,
            'trade_no': trade_obj.trade_no,
            'logistics_name': '%s Express'% site.name,
            'invoice_no': trade_obj.out_trade_no,
            'transport_type': 'EXPRESS',
            }
    form = AliPaySendGoodsForm(auto_id=False, initial=alipay_dict)
    data = get_form_data(form)
    data['sign'] = make_sign(data)
    return urllib2.urlopen(form.get_action(),urlencode(data)).read()

def alipay_dpn_check(dpn_obj):
    """
    check alipay notify
    """
    if dpn_obj.trade_status != "TRADE_FINISHED":
        return (True, 'trade status: %s'% dpn_obj.trade_status)
    return (False, None)

def alipay_ptn_check(ptn_obj):
    """
    check alipay notify
    """
    if ptn_obj.trade_status != "TRADE_FINISHED":
        return (True, 'trade status: %s'% ptn_obj.trade_status)
    return (False, None)

def alipay_show_me_the_money(sender, **kwargs):
    trade_obj = sender

def alipay_wait_seller_send_goods(sender, **kwargs):
    """
    send goods
    """
    trade_obj = sender
    if trade_obj.flag and trade_obj.trade_status == "WAIT_SELLER_SEND_GOODS":
        xmlreturn = alipay_send_goods(trade_obj)
    return

alipay_dpn_successful.connect(alipay_show_me_the_money, dispatch_uid='alipay_dpn_successful')
alipay_ptn_successful.connect(alipay_show_me_the_money, dispatch_uid='alipay_ptn_successful')
alipay_ptn_flagged.connect(alipay_wait_seller_send_goods, dispatch_uid='alipay_ptn_flagged')

