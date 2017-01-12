# -*- coding:utf-8 -*-

import uuid
from django.contrib.sites.models import Site
from django.shortcuts import render

from alipay.create_partner_trade_by_buyer.forms import AliPayPartnerTradeForm
from alipay.create_partner_trade_by_buyer.ptn.models import AliPayPTN
from alipay.helpers import make_sign, get_form_data

from alipay.create_direct_pay_by_user.forms import AliPayDirectPayForm
from alipay.create_direct_pay_by_user.dpn.models import AliPayDPN

from forms import PaymentForm


def dpn_asks_for_money(request):
    if request.method == 'GET':
        alipay_form = PaymentForm(auto_id=False)
        context = {
            "alipay_form": alipay_form,
        }
        return render(request, "pay/payment.html", context)
    # POST method
    site = Site.objects.get_current()
    pay_url = 'http://%s/'%(site.domain)
    form = PaymentForm(request.POST, auto_id=False)
    if not form.is_valid():
        context = {
            "alipay_form": form,
        }
        return render(request, "pay/payment.html", context)
    # alipay form
    item_name = ("Django Alipay example")
    alipay_dict = {
            # base
            "_input_charset": 'utf-8',
            'notify_url': '%salipay/dpn/'% pay_url,
            'return_url': '%salipay/dpn/return/'% pay_url,
            # business
            #'seller_email': '',
            'out_trade_no': uuid.uuid4().hex,
            'subject': item_name,
            'price': form.cleaned_data['price'],
            'quantity': form.cleaned_data['quantity'],
            # direct pay
            #'extra_common_param': '%s|%d'% (form.cleaned_data['price'], form.cleaned_data['quantity']),
            # partner trade
            'body': '%s|%d'% (form.cleaned_data['price'], form.cleaned_data['quantity']),
            }
    alipay_form = AliPayDirectPayForm(auto_id=False, initial=alipay_dict)
    context = {
            'payment_title': ('AliPay Payment'),
            'item_name': item_name,
            'form': form,
            'action': alipay_form.get_action(),
            'paid_form': alipay_form,
            }
    data = get_form_data(alipay_form)
    alipay_form['sign'].field.initial = make_sign(data)
    return render(request, "pay/preview.html", context)


def dpn_alipay_return(request):
    """
    alipay return with GET method
    """
    trade_status = {
            'WAIT_BUYER_PAY':('Please pay in <a href="http://www.alipay.com/"><strong>AliPay</strong></a>.'),           #等待买家付款
            'WAIT_SELLER_SEND_GOODS':('We will sent goods in a few minutes.'),   #买家已付款，等待卖家发货
            'WAIT_BUYER_CONFIRM_GOODS':('We have sent goods, please confirm in <a href="http://www.alipay.com/"><strong>AliPay</strong></a>.'), #卖家已发货，等待买家收货
            'TRADE_FINISHED':('The trade has been finished successfully.'),           #买家已收货，交易完成
            'TRADE_CLOSED':('The trade has been closed.'),             #交易中途关闭（已结束，未成功完成）
            'COD_WAIT_SELLER_SEND_GOODS':('COD No implement'),   # 等待卖家发货（货到付款）
            'COD_WAIT_BUYER_PAY':('COD: No implement'),           # 等待买家签收付款（货到付款）
            'COD_WAIT_SYS_PAY_SELLER':('COD: No implement'),      # 签收成功等待系统打款给卖家（货到付款）
            }

    info = []
    info.append(('Thank you for your payment.'))
    data = getattr(request, request.method)
    out_trade_no = data.get('out_trade_no')
    dpn_obj = []
    if out_trade_no:
        dpn_obj=AliPayDPN.objects.filter(out_trade_no=out_trade_no).order_by('-created_at')
    if not dpn_obj:
        info.append(('Please check payment status.'))
    else:
        status = dpn_obj[0].trade_status    # only check latest status
        info.append(trade_status.get(status,('Sorry, catch a error: %s.')% status))

    context = {"paid_message": ' '.join(info)}
    return render(request, "pay/paid.html", context)


def ptn_asks_for_money(request):
    if request.method == 'GET':
        alipay_form = PaymentForm(auto_id=False)
        context = {
            "alipay_form": alipay_form,
        }
        return render(request, "pay/payment.html", context)
    # POST method
    site = Site.objects.get_current()
    pay_url = 'http://%s/'%(site.domain)
    form = PaymentForm(request.POST, auto_id=False)
    if not form.is_valid():
        context = {
            "alipay_form": form,
        }
        return render(request, "pay/payment.html", context)
    # alipay form
    item_name = ("Django Alipay example")
    alipay_dict = {
            # base
            "_input_charset": 'utf-8',
            'notify_url': '%salipay/ptn/'% pay_url,
            'return_url': '%salipay/ptn/return/'% pay_url,
            # business
            #'seller_email': '',
            'out_trade_no': uuid.uuid4().hex,
            'subject': item_name,
            'price': form.cleaned_data['price'],
            'quantity': form.cleaned_data['quantity'],
            # direct pay
            #'extra_common_param': '%s|%d'% (form.cleaned_data['price'], form.cleaned_data['quantity']),
            # partner trade
            'body': '%s|%d'% (form.cleaned_data['price'], form.cleaned_data['quantity']),
            }
    alipay_form = AliPayPartnerTradeForm(auto_id=False, initial=alipay_dict)
    context = {
            'payment_title': ('AliPay Payment'),
            'item_name': item_name,
            'form': form,
            'action': alipay_form.get_action(),
            'paid_form': alipay_form,
            }
    data = get_form_data(alipay_form)
    alipay_form['sign'].field.initial = make_sign(data)
    return render(request, "pay/preview.html", context)


def ptn_alipay_return(request):
    """
    alipay return with GET method
    """
    trade_status = {
            'WAIT_BUYER_PAY':('Please pay in <a href="http://www.alipay.com/"><strong>AliPay</strong></a>.'),           #等待买家付款
            'WAIT_SELLER_SEND_GOODS':('We will sent goods in a few minutes.'),   #买家已付款，等待卖家发货
            'WAIT_BUYER_CONFIRM_GOODS':('We have sent goods, please confirm in <a href="http://www.alipay.com/"><strong>AliPay</strong></a>.'), #卖家已发货，等待买家收货
            'TRADE_FINISHED':('The trade has been finished successfully.'),           #买家已收货，交易完成
            'TRADE_CLOSED':('The trade has been closed.'),             #交易中途关闭（已结束，未成功完成）
            'COD_WAIT_SELLER_SEND_GOODS':('COD No implement'),   # 等待卖家发货（货到付款）
            'COD_WAIT_BUYER_PAY':('COD: No implement'),           # 等待买家签收付款（货到付款）
            'COD_WAIT_SYS_PAY_SELLER':('COD: No implement'),      # 签收成功等待系统打款给卖家（货到付款）
            }

    info = []
    info.append(('Thank you for your payment.'))
    data = getattr(request, request.method)
    out_trade_no = data.get('out_trade_no')
    ptn_obj = []
    if out_trade_no:
        ptn_obj=AliPayPTN.objects.filter(out_trade_no=out_trade_no).order_by('-created_at')
    if not ptn_obj:
        info.append(('Please check payment status.'))
    else:
        status = ptn_obj[0].trade_status    # only check latest status
        info.append(trade_status.get(status,('Sorry, catch a error: %s.')% status))

    context = {"paid_message": ' '.join(info)}
    return render(request, "pay/paid.html", context)
