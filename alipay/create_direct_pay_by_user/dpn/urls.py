
from django.conf.urls import url

urlpatterns = (
    url(r'^$', 'dpn', {'item_check_callable':None}, name='alipay-dpn'),
)
