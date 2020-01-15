from django.urls import path
from .views import (
    IndexView
)
from . import views

app_name = 'exchange_rates'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('post_currency', views.add_currencies, name='post_currency'),
    path('calculations', views.calculation_exchange_rates, name='calculations'),
]
