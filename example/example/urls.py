from django.conf.urls import patterns, include, url
from models import alipay_ptn_check, alipay_dpn_check

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'example.views.asks_for_money', name='home'),
    url(r'^alipay/return/$', 'example.views.alipay_return'),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^alipay/dpn/$', 'alipay.create_direct_pay_by_user.dpn.views.dpn', {'item_check_callable':alipay_dpn_check}, name='alipay-dpn'),
    url(r'^alipay/ptn/$', 'alipay.create_partner_trade_by_buyer.ptn.views.ptn', {'item_check_callable':alipay_ptn_check}, name='alipay-ptn'),

)
