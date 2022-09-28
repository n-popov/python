from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import requests
import datetime


# Create your views here.

def some_function(request):
    return HttpResponse('Hello from function some_function!')


def price(request, currency, base='USDT'):
    btc_price_response =\
        requests.get(f'https://www.binance.com/api/v3/ticker/price?symbol={currency.upper()}{base.upper()}')
    dict_with_data = btc_price_response.json()

    time = datetime.datetime.now()

    return HttpResponse(f'{currency.upper()} actual price: {float(dict_with_data["price"]) :.2f} '
                        f'{base.upper()} for time {time}')

