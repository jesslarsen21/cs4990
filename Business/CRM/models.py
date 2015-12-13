from django.db import models

import datetime
from django.contrib.auth.models import User

# Create your models here.


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return str(self.name)

class Company(models.Model):
    name = models.CharField(max_length=200, blank = True, null = True)
    website = models.URLField(max_length=200, blank = True, null = True)
    address1 = models.CharField(max_length=200, blank = True, null = True)
    address2 = models.CharField(max_length=200, blank = True, null = True)
    city = models.CharField(max_length=200, blank = True, null = True)
    state = models.CharField(max_length=200, blank = True, null = True)
    zipcode = models.CharField(max_length=200, blank = True, null = True)
    country = models.CharField(max_length=200, blank = True, null = True)
    phone = models.CharField(max_length=200, blank = True, null = True)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Companies'

class Contact(models.Model):
    company = models.ForeignKey(Company, blank = True, null = True)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    address1 = models.CharField(max_length=200, blank = True, null = True)
    address2 = models.CharField(max_length=200, blank = True, null = True)
    city = models.CharField(max_length=200, blank = True, null = True)
    state = models.CharField(max_length=200, blank = True, null = True)
    zipcode = models.CharField(max_length=200, blank = True, null = True)
    country = models.CharField(max_length=200, blank = True, null = True)
    phone = models.CharField(max_length=200, blank = True, null = True)
    email = models.EmailField(max_length=200)

    def __unicode__(self):
        return str(self.get_full_name())

    def get_full_name(self):
        return str(self.first_name + " " + self.last_name)

class Stage(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(help_text='The order this is displayed on the screen')
    description = models.TextField(blank = True, null = True)
    stage = models.IntegerField(help_text='On a scale of 0 - 100 of the stage of the pipeline')

    def __unicode__(self):
        return str(self.name)


#job
class Opportunity(models.Model):
    name = models.CharField(max_length=200)
    stage = models.ForeignKey(Stage)
    company = models.ForeignKey(Company, blank= True, null = True)
    Contact = models.ForeignKey(Contact)
    value = models.FloatField(help_text="the value of this opportunity")
    source = models.ForeignKey(Campaign, help_text="where the opportunity came from")

    user = models.ForeignKey(User)

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Opportunities'

    def __unicode__(self):
        if self.name:
            return str(self.name)
        else:
            return str(self.contact)


class Reminder(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateField()
    note = models.CharField(max_length=200)
    completed = models.BooleanField(default = False)
    def __unicode__(self):
        return str(self.opportunity) + ': ' + str(self.note)


class Report(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __unicode__(self):
        return self.name

class CallLog(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.opportunity) + " on " + self.date.strftime('%Y-%m-%d') + " by " + self.user.get_full_name()


class OpportunityStage(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    stage = models.ForeignKey(Stage)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.opportunity) + " moved to " + str(self.stage)