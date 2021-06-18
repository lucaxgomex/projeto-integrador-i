from django.db import models


# Create your models here.
class Registro(models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    account = models.ForeignKey('Conta', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Conta(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
