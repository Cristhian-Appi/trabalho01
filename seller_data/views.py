from django.shortcuts import render
from .forms import SellForm, BuyersForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from .models import Sell
from django.core.serializers import serialize
#o request busca a pagina templates por padrão
from django.core.serializers import serialize
from django.http import JsonResponse

def index(request):
    """View para index."""
    data = Sell.objects.all()
    serialized_data = serialize('json', data)
    return render(request, 'seller_data/index.html', {'data': serialized_data})

def new_sell(request):
    """View para cadastro de venda."""
    if request.method != 'POST':
        #nenhum dado submetido cria formulario em branco
        form = SellForm()
    else:
        #dados de POST submetidos, processamento
        form = SellForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index')) #usa reverse para puxar a url sem 'saber' a url, ou seja pelo name dado em urls.py (mantendo em new sell pela exigencia do trab)
        
    context = {'form': form}
    return render(request, 'seller_data/new_sell.html', context)

def buyers_number(request):
    if request.method != 'POST':
        form = BuyersForm()

    else:
        form = BuyersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('buyers_number'))
        
    context = {'form': form}
    return render(request, 'seller_data/buyers_number.html', context)

