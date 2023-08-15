from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    upc  = models.CharField(null=False, max_length=200)
    date  = models.CharField(null=True, max_length=200)
    quantite = models.CharField(null=True, max_length=200)
    name    = models.CharField(null=True, max_length=200)
    
    def __str__(self):
        return self.Name

    @classmethod
    def clear_content(cls):
        cls.objects.all().delete()

    @classmethod
    def add_data(cls, upc, name, date, quantite):
        cls.objects.create(upc=upc, name=name, date=date, quantite=quantite)

class Product_Label(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(null=True, max_length=200)

    @classmethod
    def clear_content(cls):
        cls.objects.all().delete()

    def __str__(self):
        return self.label