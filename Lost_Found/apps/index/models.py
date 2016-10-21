from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
import pytz

# Create your models here.

class Item(models.Model):
    ITEM_STATUS = (
        ('D', 'Disposed of'),
        ('R', 'Returned to Guest'),
        ('S', 'Short term storage'),
        ('L', 'Long term storage')
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
    istatus = models.CharField(max_length=1, choices=ITEM_STATUS, default='S')
    # Room it was lost in
    roomnum = models.CharField(max_length=255)
    # Guest Name (if applicable)
    guestname = models.CharField(max_length=500)

    def get_days_stored(self):
        delta = datetime.now(pytz.timezone(settings.TIME_ZONE)) - self.added
        return delta.days

    def get_status(self):
        if self.istatus == 'D':
            return 'Disposed of/Sold'
        if self.istatus == 'R':
            return 'Returned to Guest'
        if self.istatus == 'S':
            return 'Short-Term Storage'
        if self.istatus == 'L':
            return 'Long-Term Storage'
        else:
            return self.istatus + " (unknown)" # return white for anything undefined.

    def get_legal_color(self):
        # divide the number of legal days by the maximum color value
        # this way we know how much to add/subtract from red/green
        colordelim = 255 / settings.LEGAL_STORAGE_DAYS;
        # get number of days it's been stored here
        days = self.get_days_stored()
        # Calculate the value to subtract from the RGB value
        if days >= settings.LEGAL_STORAGE_DAYS: # when days >= settings.LEGAL_STORAGE_DAYS, it's just red.
            r = 255
            g = 0
            b = 0
        else:
            r = colordelim * days # Number of days times the color value to add based on LEGAL_STORAGE_DAYS
            g = 255 - r # Subtract that from 255 of green, this produces the gradiant during transition days
            b = 0 # blue is never here.

        # Return our HEX value for Django to use.
        return '#%02x%02x%02x' % (r, g, b)

    def get_status_color(self):
        if self.istatus == 'D':
            return '#FF0000' # Return red
        if self.istatus == 'R':
            return '#00FF00' # Return green
        if self.istatus == 'S':
            return '#226666' # Return a cyanish color
        if self.istatus == 'L':
            return '#FFFF00' # Return yellow
        else:
            return '#FFFFFF' # return white for anything undefined.

    # if it is greater than the legal time length then this function returns true.
    # This function returns false if it is still pending pickup and within the legal timeframe.
    def agingAudit(self):
        return self.added <= datetime.now(settings.TIME_ZONE)

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
