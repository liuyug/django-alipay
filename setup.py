#!/usr/bin/env python

import os
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-alipay',
    version='0.1',
    platforms=['noarch'],
    packages=[
        'alipay',
        'alipay.create_direct_pay_by_user',
        'alipay.create_direct_pay_by_user.dpn',
        'alipay.create_partner_trade_by_buyer',
        'alipay.create_partner_trade_by_buyer.ptn',
        'alipay.send_goods_confirm_by_platform',
    ],
    include_package_data=True,
    license='MIT',
    description='alipay api for django',
    long_description=README,
    url='https://github.com/liuyug/django-alipay',
    author='Yugang LIU',
    author_email='liuyug@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
