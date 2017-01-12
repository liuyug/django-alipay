
from django.conf.urls import url

urlpatterns = (
    url(r'^$', 'ptn', {'item_check_callable':None}, name='alipay-ptn'),
)
