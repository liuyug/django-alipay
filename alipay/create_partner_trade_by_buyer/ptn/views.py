# -*- coding:utf-8 -*-

from django.http import HttpResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .forms import AliPayPTNForm
from .models import AliPayPTN


@require_POST
@csrf_exempt
def ptn(request, item_check_callable=None):
    """
    Recevied notify from alipay by POST method
    """
    flag = None
    ptn_obj = None
    post_data = request.POST.copy()
        # cleanup data
    data = {}
    for k,v in post_data.items():
        data[k] = v
        # valid data
    form = AliPayPTNForm(data)
    if form.is_valid():
        try:
            ptn_obj = form.save(commit=False)
        except Exception, e:
            flag = 'Exception while processing: %s'% e

    else:
        flag = 'Invalid: %s'% form.errors
    if ptn_obj is None:
        ptn_obj = AliPayPTN()

       #Set query params and sender's IP address
    ptn_obj.initialize(request)

    if flag is not None:
        #We save errors in the flag field
        ptn_obj.set_flag(flag)
    else:
        ptn_obj.verify(item_check_callable)
    ptn_obj.save()
    return HttpResponse('success')


