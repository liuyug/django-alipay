
from django.conf.urls.defaults import *

urlpatterns = patterns('alipay.create_partner_trade_by_buyer.ptn.views',
    url(r'^alipay/ptn/$', 'ptn', {'item_check_callable':None}, name='alipay-ptn'),
)

