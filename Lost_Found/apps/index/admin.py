# Register your models here.
from django.contrib import admin
from Lost_Found.apps.index.models import Item, Note, PhoneNumber


class ItemAdmin(admin.ModelAdmin):
    list_display = ['guestname', 'added']
    #list_filter = ['listed', 'pub_date']
    search_fields = ['desc', 'location']
    display_fields = ['added', 'itinerary', 'desc', 'location', 'istatus', 'roomnum', 'guestname']
    date_heirachy = 'added'
    save_on_top = True


class NoteAdmin(admin.ModelAdmin):
    display_fields = ["desc", "time", "user", "item"]

class PhoneNumberAdmin(admin.ModelAdmin):
    display_fields = ["name", "number", "item"]


admin.site.register(Item, ItemAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
