from decimal import Decimal

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

    if request.method == 'POST':
        response_data = {}

        from_currency = get_object_or_404(Currency, currency_code=request.POST['from_currency'])
        to_currency = get_object_or_404(Currency, currency_code=request.POST['to_currency'])

        money = request.POST.get('money')

        result_of_convert = convert_to(
            money,
            from_currency.count_currency,
            from_currency.currency_to_bgn,
            to_currency.reverse_currency
        )
        response_data['result_of_convert'] = result_of_convert

        return render(request, 'exchange_rates/calculations.html', response_data)
    else:
        return render(request, 'exchange_rates/calculations.html', context)


def convert_to(money, count_currency, from_currency, to_currency):
    return (Decimal(money)/count_currency) * from_currency * to_currency
