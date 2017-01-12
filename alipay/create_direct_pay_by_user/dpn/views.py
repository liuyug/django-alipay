# -*- coding:utf-8 -*-

from django.http import HttpResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import AliPayDPN
from .forms import AliPayDPNForm


@require_POST
@csrf_exempt
def dpn(request, item_check_callable=None):
    """
    Recevied notify from alipay by POST method
    """
    flag = None
    dpn_obj = None
    post_data = request.POST.copy()
        # cleanup data
    data = {}
    for k,v in post_data.items():
        data[k] = v[0]
        # valid data
    form = AliPayDPNForm(data)
    if form.is_valid():
        try:
            dpn_obj = form.save(commit=False)
        except Exception, e:
            flag = 'Exception while processing: %s'% e

    else:
        flag = 'Invalid: %s'% form.errors
    if dpn_obj is None:
        dpn_obj = AliPayDPN()

       #Set query params and sender's IP address
    dpn_obj.initialize(request)

    if flag is not None:
        #We save errors in the flag field
        dpn_obj.set_flag(flag)
    else:
        dpn_obj.verify(item_check_callable)
    dpn_obj.save()

    return HttpResponse('success')


