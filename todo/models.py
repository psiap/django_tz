from django.db import models

# Create your models here.
class Client(models.Model):
    username = models.CharField(max_length=100)
    spent_money = models.CharField(max_length=100)
    gems = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class DealsFile(models.Model):
    customer = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    quantity  = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.customer
