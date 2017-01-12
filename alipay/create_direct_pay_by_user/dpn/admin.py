# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import AliPayDPN


class AliPayDPNAdmin(admin.ModelAdmin):
    date_hierarchy = 'gmt_payment'
    list_display = [
        "__unicode__", "flag", "flag_info", "out_trade_no", "trade_no",
        "extra_common_param", "trade_status", "created_at"
    ]
    search_fields = ["out_trade_no", "trade_no"]


admin.site.register(AliPayDPN, AliPayDPNAdmin)
