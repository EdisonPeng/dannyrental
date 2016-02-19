from django.contrib import admin

from .models import Home, HomePhoto
from .models import Room, RoomPhoto
from .models import About, Transportation, Reservation, ContactInfo 

class RoomPhotoInline(admin.StackedInline):
    model = RoomPhoto
    extra = 3

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomPhotoInline]

class HomePhotoInline(admin.StackedInline):
    model = HomePhoto
    extra = 3

class HomeAdmin(admin.ModelAdmin):
    inlines = [HomePhotoInline]

admin.site.register(Home, HomeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(About)
admin.site.register(Transportation)
admin.site.register(Reservation)
admin.site.register(ContactInfo)
