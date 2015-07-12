from django.db import models
from persons.models import Person

class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Community(models.Model):
    name = models.CharField(max_length=254)
    purpose = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='communities', null=True)
    quantity = models.IntegerField()
    sector = models.ForeignKey(Sector)

    def __unicode__(self):
        return self.name

class Objective(models.Model):
    description = models.CharField(max_length=200)
    community = models.ForeignKey(Community, related_name='objectives')

    def __unicode__(self):
        return self.description

class TypeSocialNetwork(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class SocialNetwork(models.Model):
    link = models.CharField(max_length=300)
    type_social = models.ForeignKey(TypeSocialNetwork)
    community = models.ForeignKey(Community)

class CommunityRole(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Member(models.Model):
    community =  models.ForeignKey(Community)
    role = models.ForeignKey(CommunityRole)
    person = models.ForeignKey(Person)

    def __unicode__(self):
        return self.community.name + '-' + self.person.first_name + ' ' + self.person.last_name