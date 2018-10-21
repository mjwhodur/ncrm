from django.db import models


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=50)
    Mnemonic = models.CharField(max_length=5)


class Project(models.Model):
    Name = models.CharField(max_length=500)
    Category = models.ForeignKey(Category, on_delete=models.deletion.DO_NOTHING)
    Description = models.TextField(verbose_name='Opis')


class Severity(models.Model):
    Level = models.IntegerField(default=0)
    Name = models.CharField(max_length=50, blank=False)


class Patch(models.Model):
    Number = models.CharField(max_length=500)
    Name = models.CharField(max_length=500)


class Issue(models.Model):
    Number = models.CharField(max_length=500)
    Name = models.CharField(max_length=500)
    Description = models.TextField(max_length=65536)


class IssuePatch(models.Model):
    Issue = models.ForeignKey(Issue, on_delete=models.deletion.CASCADE)
    Patch = models.ForeignKey(Patch, on_delete=models.deletion.CASCADE)


class IssueAttachments(models.Model):
    Issue = models.ForeignKey(Issue, on_delete=models.deletion.CASCADE)
