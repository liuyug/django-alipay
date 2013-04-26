# -*- coding:utf-8 -*-
from django.conf import settings

# COD Cash On Delivery 货到付款

# 合作者身份 ID，以 2088 开头的 16 位纯数字组成
PARTNER = getattr(settings, 'ALIPAY_PARTNER', '2088123456789012')
# private key for sign
PRIVATE_KEY = getattr(settings, 'ALIPAY_PRIVATE_KEY', 'unknown key')
SELLER_ID = getattr(settings, 'ALIPAY_SELLER_ID', 'unknow seller id')

# 支付宝网关
ALIPAY_GATEWAY = 'https://mapi.alipay.com/gateway.do'

# 支付宝通知 IP
ALIPAY_NOTIFY_IP = getattr(settings, 'ALIPAY_NOTIFY_IP',('121.0.26.0/23', '110.75.128.0/19'))


ALIPAY_DATE_FORMAT = ('%Y-%m-%d %H:%M:%S',)

SERVICE = (
        'create_direct_pay_by_user',    # 即时到帐
        'create_partner_trade_by_buyer',    # 担保交易
        'send_goods_confirm_by_platform',   # 确认发货
        'trade_create_by_buyer',            # 标准双接口
        )

PAYMENT_TYPE = (
        '1',    #商品购买
        '2',    #服务购买
        '3',    #网络拍卖
        '4',    #捐赠
        '5',    #邮费补偿
        '6',    #奖金
        '7',    #基金购买
        '8',    #机票购买
        )
PAYMETHOD = (
        'creditPay',    # 'credit payment'    # 需开通信用支付
        'directPay',    # 'direct payment'    # 余额支付，不能设置 defaultbank 参数
        'bankPay',      # 'bank payment directly'   # 需开通纯网关，需设置 defaultbank
        'cash',         # 'paid by cash'
        'cartoon',      # 'paid by bank card thourgh alipay gateway'
        )

LOGISTICS_TYPE = (
        'POST',     # 平邮
        'EXPRESS',  # 其他快递
        'EMS',      # EMS
        )
LOGISTICS_PAYMENT = (
        'BUYER_PAY',    # 物流买家承担运费
        'SELLER_PAY',   # 物流卖家承担运费
        'BUYER_PAY_AFTER_RECEIVE',  # 买家到货付款，运费显示但不计入总价
        )

#交易状态
TRADE_STATUS = (
        'WAIT_BUYER_PAY',           #等待买家付款
        'WAIT_SELLER_SEND_GOODS',   #买家已付款，等待卖家发货
        'WAIT_BUYER_CONFIRM_GOODS', #卖家已发货，等待买家收货
        'TRADE_FINISHED',           #买家已收货，交易完成
        'TRADE_CLOSED',             #交易中途关闭（已结束，未成功完成）
        'COD_WAIT_SELLER_SEND_GOODS',   # 等待卖家发货（货到付款）
        'COD_WAIT_BUYER_PAY',           # 等待买家签收付款（货到付款）
        'COD_WAIT_SYS_PAY_SELLER',      # 签收成功等待系统打款给卖家（货到付款）
        )



