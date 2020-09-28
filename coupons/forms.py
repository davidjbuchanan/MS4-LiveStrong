from django import forms
from .models import Coupon


class CouponApplyForm(forms.Form):
    code = forms.CharField()

    class Meta:
        model = Coupon
        fields = (
            'code',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'code': 'Enter coupon code',
        }

        self.fields['code'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]}'

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class CouponForm(forms.ModelForm):

    class Meta:
        model = Coupon
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'code': 'Enter coupon code',
            'valid_from': 'yyyy-mm-dd hh:mm:ss',
            'valid_to': 'yyyy-mm-dd hh:mm:ss',
            'discount': 'discount as a %',
            'active': ''
        }

        self.fields['code'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
