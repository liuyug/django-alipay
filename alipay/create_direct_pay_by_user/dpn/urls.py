
from django.conf.urls.defaults import *

urlpatterns = patterns('alipay.create_direct_pay_by_user.dpn.views',
    url(r'^$', 'dpn', {'item_check_callable':None}, name='alipay-dpn'),
)

