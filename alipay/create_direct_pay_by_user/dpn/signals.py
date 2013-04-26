from django.dispatch import Signal

# Sent when a payment is successfully processed.
alipay_dpn_successful = Signal()

alipay_dpn_flagged = Signal()
