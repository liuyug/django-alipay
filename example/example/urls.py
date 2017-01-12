from django.conf.urls import include, url
from models import alipay_ptn_check, alipay_dpn_check

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from . import views
from alipay.create_direct_pay_by_user.dpn import views as dpn_views
from alipay.create_partner_trade_by_buyer.ptn import views as ptn_views


urlpatterns = (
    url(r'^$', views.asks_for_money, name='home'),
    url(r'^alipay/return/$', views.alipay_return),

    # alipay urls
    url(r'^alipay/dpn/$',
        dpn_views.dpn,
        {'item_check_callable':alipay_dpn_check},
        name='alipay-dpn'),
    url(r'^alipay/ptn/$',
        ptn_views.ptn,
        {'item_check_callable':alipay_ptn_check},
        name='alipay-ptn'),
    # admin urls
    url(r'^admin/', admin.site.urls),
)
