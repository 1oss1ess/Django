from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100, unique=True)
    currency_code = models.CharField(max_length=3, unique=True)
    currency_to_bgn = models.DecimalField(max_digits=22, decimal_places=9)
    reverse_currency = models.DecimalField(max_digits=22, decimal_places=9)
    count_currency = models.DecimalField(max_digits=22, decimal_places=9)

    class Meta:
        ordering = ('currency_code',)
        verbose_name_plural = 'currencies'

    def __str__(self):
        return '{} : {}'.format(self.currency_code, self.currency_to_bgn)
