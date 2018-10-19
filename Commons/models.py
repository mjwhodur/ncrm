from django.db import models


# Create your models here.

class Company(models.Model):
    """
        Holds data about Company issuing document. Note, that documents are system-wide.
    """
    IdentificationNumber = models.CharField(max_length=50)
    TaxID = models.CharField(max_length=50)

class Divisions(models.Model):
    pass

class Document(models.Model):
    pass

class DocumentSettlement(models.Model):
    pass

class ItemTypes(models.Model):
    Name = models.CharField(max_length=50)


class ItemRecord(models.Model):
    pass
