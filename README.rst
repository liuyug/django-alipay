=======
alipay
=======
|version| |download|

alipay api for django

Quick start
-----------

1. Add "alipay" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'alipay...',
    )

2. Include the alipay URLconf in your project urls.py like this::

    url(r'^alipay/ptn/', include('alipay.create_partner_trade_by_buyer.ptn.urls')),

3. Run `python manage.py syncdb` to create the alipay models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/alipay/ to participate in the poll.

Please see example!!

.. |version| image:: https://img.shields.io/pypi/v/django-alipay.png
    :target: https://pypi.python.org/pypi/django-alipay/
    :alt: Version

.. |download| image:: https://img.shields.io/pypi/dm/django-alipay.png
    :target: https://pypi.python.org/pypi/django-alipay/
    :alt: Downloads
