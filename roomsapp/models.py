from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class HotelRoom(models.Model):
    """Номера отеля"""
    title = models.CharField("Название", max_length=500)
    description = models.CharField("Описание", max_length=500)
    image = models.ImageField("Фото", upload_to="room/", null=True, blank=True)
    price = models.PositiveIntegerField("Цена")

    class Meta:
        verbose_name = "Номер отеля"
        verbose_name_plural = "Номера отеля"

    def __str__(self):
        return self.title


class HotelObjects(models.Model):
    """Объекты номера(телевизор, кровать и т.д)"""
    title = models.CharField("Название", max_length=250)
    sub_title = models.CharField("Описание", max_length=250, default='')
    icon = models.CharField("Иконка", max_length=250)
    about_room = models.ForeignKey(
        HotelRoom,
        on_delete=models.CASCADE,
        verbose_name="О номере",
        related_name="about_room"
    )

    class Meta:
        verbose_name = "Объект номера"
        verbose_name_plural = "Объекты номера"

    def __str__(self):
        return self.title


class RatingsRooms(models.Model):
    """Оценка сервиса номеров"""
    title = models.CharField("Название", max_length=250)
    rating = models.FloatField("Оценка", validators=[MinValueValidator(0), MaxValueValidator(10)])
    services = models.ForeignKey(
        HotelRoom,
        on_delete=models.CASCADE,
        verbose_name="Оценка сервиса",
        related_name="services"
    )

    class Meta:
        verbose_name = "Оценка сервиса номеров"
        verbose_name_plural = "Оценки сервиса номеров"

    def __str__(self):
        return self.title


class BookingRoom(models.Model):
    """Модель бронирования номеров"""
    entry_date = models.DateField("Дата заезда")
    depart_date = models.DateField("Дата выезда")
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    comment = models.TextField("Комментарий", max_length=2500, blank=True)
    adult = models.PositiveIntegerField("Взрослые", default=0)
    children = models.PositiveIntegerField("Дети", default=0)
    rooms = models.ForeignKey(
        HotelRoom,
        verbose_name="Заказанный номер",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_room')

    class Meta:
        verbose_name = "Заказанный номер"
        verbose_name_plural = "Забронированные номера"

    def __str__(self):
        return self.name
