from django.db import models
from authentication.models import User
class Itens(models.Model):
    code_item = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stock_quantity = models.IntegerField(default=0)
    price = models.FloatField()
    image = models.ImageField(
        upload_to='itens_images/', null=True, blank=True)

    def __str__(self):
        return f"Nome = {self.name}"

    def repor_estoque(self, quantidade):
        self.stock_quantity += quantidade
        self.save()

    def retirar_estoque(self, quantidade):
        if quantidade > self.stock_quantity:
            raise ValueError("Estoque insuficiente.")
        self.stock_quantity -= quantidade
        self.save()

    def descricao(self):
        return (
            f"Nome: {self.name} - Código: {self.code_item} - "
            f"Categoria: {self.category} - Descrição: {self.description} - "
            f"Estoque: {self.stock_quantity}"
        )


class Company(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    password = models.CharField(max_length=128)
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nome: {self.name} - CNPJ: {self.cnpj}"
