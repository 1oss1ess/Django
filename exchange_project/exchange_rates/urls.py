from django.urls import path

from .views import (
    IndexView,
    add_currencies,
    calculation_exchange_rates
)

app_name = 'exchange_rates'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('post_currency', add_currencies, name='post_currency'),
    path('calculations', calculation_exchange_rates, name='calculations'),
]
