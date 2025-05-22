from django.db import models


class Itens(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stock_quantity = models.IntegerField(default=0)
    price = models.FloatField()

    def __str__(self):
        return self.name

    def repor_estoque(self, quantidade):
        self.stock_quantity += quantidade
        self.save()

    def retirar_estoque(self, quantidade):
        if quantidade > self.stock_quantity:
            raise ValueError("Estoque insuficiente.")
        self.stock_quantity -= quantidade
        self.save()

    def descricao(self):
        return f"Nome: {self.name} - Código: {self.code} - Categoria: {self.category} - Descricao: {self.description} - Estoque: {self.stock_quantity}"


class ItemImage(models.Model):
    item = models.ForeignKey(Itens, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return f"Imagem de {self.item.name}"


class Empresa(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    logo = models.ImageField(upload_to='logo/')
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"Nome: {self.name} - CNPJ: {self.cnpj}"
