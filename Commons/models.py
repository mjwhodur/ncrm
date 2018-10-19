from django.db import models


# Create your models here.

class Company(models.Model):
    """
        Holds data about Company issuing document. Note, that documents are system-wide. You may control many companies.
    """
    IdentificationNumber = models.CharField(max_length=50)
    TaxID = models.CharField(max_length=50)
    Name = models.CharField(max_length=500)

class Divisions(models.Model):
    Company = models.ForeignKey(Company)
    Mnemonic = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)

class Document(models.Model):
    pass

class DocumentSettlement(models.Model):
    pass

class ItemTypes(models.Model):
    Name = models.CharField(max_length=50)


class ItemRecord(models.Model):
    pass
