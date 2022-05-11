from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import HotelObjects, RatingsRooms, HotelRoom, BookingRoom


class RoomsSerializer(ModelSerializer):
    """Объекты номера(телевизор, кровать и т.д)"""

    class Meta:
        model = HotelRoom
        fields = '__all__'


class HotelObjectsSerializer(serializers.ModelSerializer):
    """Объекты номера(телевизор, кровать и т.д)"""

    class Meta:
        model = HotelObjects
        fields = ('title',
                  'sub_title',
                  'icon'
                  )


class RatingsRoomsSerializer(serializers.ModelSerializer):
    """Оценка сервиса номеров"""

    class Meta:
        model = RatingsRooms
        fields = ('title',
                  'rating',
                  )


class HotelRoomsSerializer(serializers.ModelSerializer):
    """Номера отеля"""

    about_room = HotelObjectsSerializer(read_only=True, many=True)
    # about_room = serializers.StringRelatedField(many=True)
    services = RatingsRoomsSerializer(read_only=True, many=True)
    image = serializers.ImageField(use_url='image.url')

    class Meta:
        model = HotelRoom
        fields = ('id',
                  'title',
                  'image',
                  'description',
                  'about_room',
                  'services',
                  )


class BookingRoomSerializer(serializers.ModelSerializer):
    """Бронирование номера отеля"""

    class Meta:
        model = BookingRoom
        fields = '__all__'

    def create(self, request):
        results = request.pop('rooms')
        booking = BookingRoom.objects.create(rooms=results, **request)
        return booking


class BookingHotelSerialize(serializers.ModelSerializer):
    """Сериализация номеров по id"""

    class Meta:
        model = HotelRoom
        fields = ('id', 'title')


class BookingRoomListSerializer(serializers.ModelSerializer):
    """Сериализация списка зобронированных номеров"""
    rooms = BookingHotelSerialize(read_only=True)

    class Meta:
        model = BookingRoom
        fields = (
            'entry_date',
            'depart_date',
            'name',
            'phone',
            'comment',
            'adult',
            'children',
            'rooms',
        )
