from django.db import models

from persons.models import Town, Person
from communities.models import Community

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    latitude = models.DecimalField(null=True, blank=True, max_digits=23, decimal_places=20)
    longitude = models.DecimalField(null=True, blank=True, max_digits=23, decimal_places=20)
    minimum_assistant = models.IntegerField()
    count_potential_attendee = models.IntegerField(null=True)
    count_assistant = models.IntegerField(null=True)
    count_up_vote = models.IntegerField(null=True)
    count_down_vote = models.IntegerField(null=True)
    image = models.ImageField(null=True, blank=True, upload_to='activities')
    town = models.ForeignKey(Town)
    community = models.ForeignKey(Community)

    def __unicode__(self):
        return self.name

class Vote(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    type_vote = models.IntegerField()
    person = models.ForeignKey(Person)
    activity = models.ForeignKey(Activity)

class PotentialAttendee(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(Person)
    activity = models.ForeignKey(Activity)

class Assistant(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(null=True, blank=True, max_digits=23, decimal_places=20)
    longitude = models.DecimalField(null=True, blank=True, max_digits=23, decimal_places=20)
    person = models.ForeignKey(Person)
    activity = models.ForeignKey(Activity)