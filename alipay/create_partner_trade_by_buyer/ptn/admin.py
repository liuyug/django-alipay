# -*- coding: utf-8 -*-

from django.contrib import admin
from alipay.create_partner_trade_by_buyer.ptn.models import AliPayPTN

class AliPayPTNAdmin(admin.ModelAdmin):
    date_hierarchy = 'gmt_payment'
    list_display = [
        "__unicode__", "flag", "flag_info", "out_trade_no", "trade_no", "body", 
        "trade_status", "created_at"
    ]
    search_fields = ["out_trade_no", "trade_no"]


admin.site.register(AliPayPTN, AliPayPTNAdmin)
