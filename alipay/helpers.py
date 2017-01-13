# -*- coding:utf-8 -*-

import hashlib
import socket
import struct
import urllib

from . import conf

def address_in_network(ip, net):
    """
    Is an address in a network
    ip: 192.168.2.2
    net:("192.168.2.0/24",)
    """
    ipaddr = struct.unpack('L',socket.inet_aton(ip))[0]
    for cur_net in net:
        netaddr,bits = cur_net.split('/')
        netmask = struct.unpack('L',socket.inet_aton(netaddr))[0] & ((2<<int(bits)-1) - 1)
        if ipaddr & netmask == netmask:
            return True
    return False

def make_sign(data, private_key=conf.PRIVATE_KEY):
    query_list = []
    hash = data.get('sign_type','MD5')
    for k,v in data.items():
        if k == 'sign' or k == 'sign_type':
            continue
        query_list.append('%s=%s'% (k,v))

    query_list.sort()
    text = '%s%s'% ('&'.join(query_list), private_key)
    if hash == 'MD5':
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        sign = md5.hexdigest()
    else:
        raise NotImplementedError
    return sign

def duplicate_out_trade_no(trade_obj):
    query = trade_obj._default_manager.filter(out_trade_no=trade_obj.out_trade_no)
    query = query.filter(trade_status=trade_obj.trade_status)
    return query.count() > 0

def get_form_data(form):
    """
    if form is bound, return bound data
    if form is initial, return initial data
    """
    data = {}
    if form.is_bound:
        data = form.data
    else:   # unbound data
        for name, field in form.fields.items():
            if form.initial.has_key(name):
                data[name] = form.initial[name]
            elif field.initial:
                data[name] = field.initial
    return data

def urldecode(query):
    data = {}
    query_list = query.split('&')
    for kv in query_list:
        if kv.find('='):
            k,v = map(urllib.unquote_plus, kv.split('='))
            data[k] = v
    return data

