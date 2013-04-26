#!/usr/bin/env python

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-alipay',
    version='0.1',
    packages=[
        'alipay',
        'alipay.create_direct_pay_by_user',
        'alipay.create_direct_pay_by_user.dpn',
        'alipay.create_partner_trade_by_buyer',
        'alipay.create_partner_trade_by_buyer.ptn',
        'alipay.send_goods_confirm_by_platform',
    ],
    include_package_data=True,
    license='GPLv3 License',
    description='alipay api for django',
    long_description=README,
    url='http://www.example.com/',
    author='Yugang LIU',
    author_email='liuyug@gmail.com',
)
