from django.urls import path

from .views import (
    IndexView,
    add_currencies,
    calculation_exchange_rates,
    crawler_view
)

app_name = 'exchange_rates'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('post_currency', add_currencies, name='post_currency'),
    path('calculations', calculation_exchange_rates, name='calculations'),
    path('crawler', crawler_view, name='crawler'),
]
