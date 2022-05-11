from django.contrib import admin

from .models import HotelObjects, RatingsRooms, HotelRoom, BookingRoom


class HotelObjectsAdmin(admin.StackedInline):
    model = HotelObjects
    extra = 1
    show_change_link = True


class RatingsRoomsAdmin(admin.StackedInline):
    model = RatingsRooms
    extra = 1
    show_change_link = True


@admin.register(HotelRoom)
class HotelRoomsAdmin(admin.ModelAdmin):
    """Номера отеля"""
    list_display = ("title", "description")
    search_fields = ("title",)
    inlines = [HotelObjectsAdmin, RatingsRoomsAdmin]


@admin.register(BookingRoom)
class BookingRoomAdmin(admin.ModelAdmin):
    """Бронь номера отеля"""
    list_display = ("name", "phone", "entry_date", "depart_date", "adult", "children")
    search_fields = ("name",)
