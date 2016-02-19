from django.db import models

class Home(models.Model):
    room_photo = models.ImageField(upload_to='images/home_photo/')
    about_photo = models.ImageField(upload_to='images/home_photo/')
    transportation_photo = models.ImageField(upload_to='images/home_photo/')

    def __unicode__(self):
        return "Home"

class HomePhoto(models.Model):
    room = models.ForeignKey(Home)
    photo = models.ImageField(upload_to='images/about_photo/')
    description = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.description

class About(models.Model):
    description = models.TextField()

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    equipment = models.TextField()
    note = models.TextField(blank=True)
    price = models.IntegerField()
    fri_price = models.IntegerField()
    sat_price = models.IntegerField()

    def __unicode__(self):
        return self.name

class RoomPhoto(models.Model):
    room = models.ForeignKey(Room)
    photo = models.ImageField(upload_to='images/room_photo/')

class Transportation(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Reservation(models.Model):
    description = models.TextField()

class ContactInfo(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    line = models.CharField(max_length=50)
    facebook = models.URLField()
    facebook_des = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
