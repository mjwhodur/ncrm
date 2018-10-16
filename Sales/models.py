from django.db import models
from CRM.models import Contractor
# Create your models here.

class Offering(models.Model):
    Number = models.CharField(max_length=50, null=False)
    Contractor = models.ForeignKey(Contractor)

class Order(models.Model):
    Number = models.CharField(max_length=50, null=False)
    Contractor = models.ForeignKey(Contractor)

class SaleDocument(models.Model):
    Number = models.CharField(max_length=50, null=False)
    Contractor = models.ForeignKey(Contractor)

