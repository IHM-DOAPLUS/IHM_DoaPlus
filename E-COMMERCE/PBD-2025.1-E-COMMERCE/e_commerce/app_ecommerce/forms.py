from django import forms
from app_ecommerce.models import Itens, Empresa


class EmpresaLogin(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = Empresa
        fields = ['cnpj', 'password']


class RegisterItem(forms.ModelForm):
    class Meta:
        model = Itens
        fields = ['code_item', 'name', 'category',
                  'description', 'stock_quantity', 'price']


class RegisterEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['name', 'cnpj', 'logo', 'password']
