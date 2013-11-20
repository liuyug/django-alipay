
from django.conf.urls import patterns, url

urlpatterns = patterns('alipay.create_partner_trade_by_buyer.ptn.views',
    url(r'^$', 'ptn', {'item_check_callable':None}, name='alipay-ptn'),
)

