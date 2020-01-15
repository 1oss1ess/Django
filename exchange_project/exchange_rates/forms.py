from django import forms

from .models import Currency


class PostCurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('name', 'currency_code', 'count_currency', 'currency_to_bgn', 'reverse_currency')
