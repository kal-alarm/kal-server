import graphene

from graphene_django.types import DjangoObjectType

from kalalarm.models import Device, Room, DeviceRoomList


class DeviceType(DjangoObjectType):
    class Meta:
        model = Device

class RoomType(DjangoObjectType):
    class Meta:
        model = Room

class DeviceRoomListType(DjangoObjectType):
    class Meta:
        model = DeviceRoomList


class Query(graphene.AbstractType):
    all_devices = graphene.List(DeviceType)
    all_rooms = graphene.List(RoomType)

    def resolve_all_devices(self, args, context, info):
        return Device.objects.all()

    def resolve_all_rooms(self, args, context, info):
        # We can easily optimize query count in the resolve method
        return Room.objects.all()