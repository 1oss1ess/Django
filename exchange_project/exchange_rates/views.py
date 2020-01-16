from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.list import ListView

from .forms import PostCurrencyForm
from .models import Currency


class IndexView(ListView):
    model = Currency
    context_object_name = 'currency_list'
    template_name = 'exchange_rates/home.html'


def add_currencies(request):
    if request.method == 'POST':
        form = PostCurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('exchange_rates:home'))
    else:
        form = PostCurrencyForm()
    return render(request, 'exchange_rates/post-currency.html', {'form': form})


def calculation_exchange_rates(request):
    currencies = Currency.objects.all()
    context = {
        'currencies': currencies
    }
    if request.is_ajax():

        from_currency = get_object_or_404(Currency, currency_code=request.GET['from_currency'])
        to_currency = get_object_or_404(Currency, currency_code=request.GET['to_currency'])

        money = request.GET['money']

        result_of_convert = convert_to(
            money,
            from_currency.count_currency,
            from_currency.currency_to_bgn,
            to_currency.reverse_currency
        )

        response_data = {}
        response_data['result_of_convert'] = result_of_convert

        return JsonResponse(response_data)

    return render(request, 'exchange_rates/calculations.html', context)


def convert_to(money, count_currency, from_currency, to_currency):
    return (Decimal(money)/count_currency) * from_currency * to_currency
