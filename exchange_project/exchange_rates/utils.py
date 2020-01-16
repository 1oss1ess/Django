import requests

from exchange_rates.models import Currency
from decimal import Decimal

def crawling():
    url = 'https://www.bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm?download=csv&search=&lang=BG'

    url_request = requests.get(url)

    exchange_rates = url_request.text

    exchange_rates = exchange_rates.split('\n')

    for exchange_rate in exchange_rates[2:]:

        data = exchange_rate.split(',')
        if 'Забележка:' in data[0]:
            break
        count_currency = Decimal(data[3])
        currency_to_bgn = Decimal(data[4])
        reverse_currency = Decimal(data[5])
        
        import pdb;
        pdb.set_trace()

        Currency.objects.update_or_create(name=data[1],
                                          currency_code=data[2],
                                          defaults={
                                              'count_currency': count_currency,
                                              'currency_to_bgn': currency_to_bgn,
                                              'reverse_currency': reverse_currency,
                                          }
                                          )
    return 'Refresh exchange rates'

