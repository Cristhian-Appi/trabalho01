from django import forms
from .models import Sell, Buyers


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['buyer_name', 'product_value', 'product_name', 'text']
        labels = {
            'buyer_name': 'Nome do Comprador',
            'product_value': 'Valor do Produto',
            'product_name': 'Nome do Produto',
            'text': 'Descrição'          
        }

class BuyersForm(forms.ModelForm):
    class Meta:
        model = Buyers
        fields = ['buyers_number']
        labels = {
            'buyers_number': 'Número de Compradores',
 
        }