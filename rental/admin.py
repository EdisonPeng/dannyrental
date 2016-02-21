from django.contrib import admin

from .models import Home, HomePhoto
from .models import Room, RoomPhoto
from .models import Reservation, TopicContent
from .models import About, Transportation, ContactInfo

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

class TopicContentInline(admin.StackedInline):
    model = TopicContent
    extra = 3

class ReservationAdmin(admin.ModelAdmin):
    inlines = [TopicContentInline]

admin.site.register(Home, HomeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(About)
admin.site.register(Transportation)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ContactInfo)
