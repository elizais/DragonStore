from django.db import models


class Dragons(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    teste_food = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    quantity_stok = models.IntegerField(default=0)


class Buyers(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    cellphone = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    dragon = models.ForeignKey(Dragons, on_delete=models.CASCADE, null=True, blank=True)

