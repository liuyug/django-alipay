
from django.conf.urls import patterns, url

urlpatterns = patterns('alipay.create_direct_pay_by_user.dpn.views',
    url(r'^$', 'dpn', {'item_check_callable':None}, name='alipay-dpn'),
)

