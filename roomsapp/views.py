from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HotelRoom, BookingRoom
from .serializers import HotelRoomsSerializer, BookingRoomSerializer, BookingRoomListSerializer, RoomsSerializer


class HotelRoomsModelViewSet(viewsets.ModelViewSet):
    queryset = HotelRoom.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.AllowAny]


class HotelRoomsList(generics.ListAPIView):
    """Список номеров отеля"""
    permission_classes = [permissions.AllowAny]
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomsSerializer


class BookingRoomRecordView(generics.ListCreateAPIView):
    """Список забронированных номеров"""
    permission_classes = [permissions.AllowAny]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer


# class BookingRoomRecord(generics.CreateAPIView):
#     """Запись брони в БД"""
#     permission_classes = [permissions.AllowAny]
#     queryset = BookingRoom.objects.all()
#     serializer_class = BookingRoomSerializer

class HotelRoomView(generics.RetrieveAPIView):
    """Детальный номер"""
    permission_classes = [permissions.AllowAny]
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomsSerializer



