from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("<center><h2>how to use</h2></center>")


def buy(request, user_id, crypto_currency, amount):
    # TODO check user exists
    # TODO check user has enough credit
    # TODO check amount, if less than 10 dollars, add to queue, else buy directly from exchange
    return JsonResponse({"result": "ok"})


def queue_manager():
    # TODO check queue and start buying from exchange if each crypto_currency is equal or more than 10$
    pass


def buy_from_exchange():
    return True
