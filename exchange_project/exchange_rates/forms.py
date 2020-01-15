from django import forms

from .models import Currency


class PostCurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('name', 'course_code', 'count_currency', 'course_to_bgn', 'reverse_course')
