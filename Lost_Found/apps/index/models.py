from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Item(models.Model):
    ITEM_STATUS = (
        ('D', 'Disposed of'),
        ('R', 'Returned to Guest'),
        ('SS', 'Short term storage'),
        ('LS', 'Long term storage')
    )

    # Item description
    desc = models.TextField()
    # PMS itinerary
    itinerary = models.CharField(max_length=255)
    # Date Added to Lost+Found
    added = models.DateTimeField(auto_now=True)
    # Item's location
    location = models.CharField(max_length=255)
    # Item's current status
    status = models.CharField(max_length=1, choices=ITEM_STATUS)
    # Room it was lost in
    roomnum = models.CharField(max_length=255)


    def __unicode__(self):
		return unicode(self.name)

    # if it is greater than the legal time length then this function returns true.
    # This function returns false if it is still pending pickup and within the legal timeframe.
    def agingAudit(self):
        return added <= datetime.now()

    class Admin:
        pass


class Note(models.Model):

    # note content
    desc = models.TextField()
    # note date/Time
    time = models.DateTimeField(auto_now=True)
    # note user
    user = models.ForeignKey(User)
    # The item the note is attached to
    item = models.ForeignKey(Item)

    class Admin:
        pass

class PhoneNumber(models.Model):

    # Name for the phone number
    name = models.CharField(max_length=255)
    # Phone number field.
    number = models.CharField(max_length=15)
    # Item it references
    item = models.ForeignKey(Item)

    class Admin:
        pass
