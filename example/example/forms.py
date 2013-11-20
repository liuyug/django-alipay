# -*- encoding: utf-8 -*-

from django import forms

class PaymentForm(forms.Form):
    price = forms.IntegerField(label=('Item price'), initial=1)
    quantity = forms.IntegerField(label=('Quantity'), initial=1)

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

    def get_currency(self):
        return self.currency

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity != None and quantity < 1:
            self._errors['quantity'] = self.error_class([('greater than or equal to one')])
            del self.cleaned_data['quantity']
        return quantity

    def as_table(self):
        return self._html_output(
                normal_row = u'<tr%(html_class_attr)s><th>%(label)s</th><td>%(field)s</td><td>%(errors)s</td></tr>',
                error_row = u'%s',
                row_ender = u'',
                help_text_html = u'%s',
                errors_on_separate_row = False)


