from django.dispatch import Signal

# Sent when a payment is successfully processed.
alipay_ptn_successful = Signal()

alipay_ptn_flagged = Signal()
