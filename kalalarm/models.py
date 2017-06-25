from django.db import models

# Create your models here.

class Device(models.Model):
    nickname = models.CharField(max_length=100)
    uuid = models.CharField(max_length=200, null=False)
    push_token = models.CharField(max_length=200, null=False)
    os = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nickname

class Room(models.Model):
    name = models.CharField(max_length=100)
    alarm_date = models.IntegerField()
    alarm_time = models.TimeField(null=False)
    is_repeat = models.BooleanField(default=False)
    alarm_ring_name = models.CharField(max_length=500, null=True)
    max_device = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class DeviceRoomList(models.Model):
    room = models.ForeignKey(Room, related_name='devices')
    device = models.ForeignKey(Device, related_name='rooms')

    is_exit = models.BooleanField(default=False)
    is_host = models.BooleanField(default=False)