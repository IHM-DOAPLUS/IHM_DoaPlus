from django import forms
from app_ecommerce.models import Itens, Empresa


class EmpresaLogin(forms.ModelForm):
    cnpj = forms.CharField(label='CPNJ', max_length=14)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = Empresa
        fields = ['cnpj',
                  'password',]


class RegisterItem(forms.ModelForm):
    code = forms.CharField(label='CODIGO', max_length=100)
    name = forms.CharField(label='NOME', max_length=100)
    category = forms.CharField(label='CATEGORIA', max_length=100)
    description = forms.CharField(label='DESCRICAO', max_length=100)
    stock_quantity = forms.IntegerField(label='ESTOQUE')
    price = forms.FloatField(label='PRECO')

    class Meta:
        model = Itens
        fields = ['code',
                  'name',
                  'category',
                  'description',
                  'stock_quantity',
                  'price',
                  ]
