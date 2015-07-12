from django.db import models

# Create your models here.\
class Sex(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class DocumentType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Departament(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Town(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Departament)

    def __unicode__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.IntegerField()
    direction = models.CharField(max_length=250)
    birth_date = models.DateField()
    email = models.EmailField(max_length=150)
    id_number = models.CharField(max_length=100)
    confirmation = models.NullBooleanField(null=True)
    password = models.CharField(max_length=100)
    sex = models.ForeignKey(Sex)
    document_type = models.ForeignKey(DocumentType)
    town = models.ForeignKey(Town)
    id_device = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name