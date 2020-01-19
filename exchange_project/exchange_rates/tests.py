from decimal import Decimal

from django.test import TestCase

from .models import Currency
from .views import convert_to


class TestCurrencyCase(TestCase):

    def setUp(self):
        self.brl = Currency(name='Бразилски реал',
                            currency_code='BRL',
                            currency_to_bgn=Decimal('4.21606'),
                            reverse_currency=Decimal('2.37188'),
                            count_currency=Decimal('10'))

        self.usd = Currency(name='Щатски долар',
                            currency_code='USD',
                            currency_to_bgn=Decimal('1.76074'),
                            reverse_currency=Decimal('0.567943'),
                            count_currency=Decimal('1'))

        self.krw = Currency(name='Южнокорейски вон',
                            currency_code='KRW',
                            currency_to_bgn=Decimal('1.51807'),
                            reverse_currency=Decimal('658.731'),
                            count_currency=Decimal('1000'))

    def test_convert_5BRL_to_KRW(self):
        result = convert_to(Decimal(5), self.brl.count_currency, self.brl.currency_to_bgn, self.krw.reverse_currency)
        self.assertEqual(result, Decimal('1388.624709930'))

    def test_convert_1BRL_to_KRW(self):
        result = convert_to(Decimal(1), self.brl.count_currency, self.brl.currency_to_bgn, self.krw.reverse_currency)
        self.assertEqual(result, Decimal('277.724941986'))

    def test_convert_1BRL_to_USD(self):
        result = convert_to(Decimal(1), self.brl.count_currency, self.brl.currency_to_bgn, self.usd.reverse_currency)
        self.assertEqual(result, Decimal('0.239448176458'))

    def test_convert_3BRL_to_USD(self):
        result = convert_to(Decimal(3), self.brl.count_currency, self.brl.currency_to_bgn, self.usd.reverse_currency)
        self.assertEqual(result, Decimal('0.718344529374'))
