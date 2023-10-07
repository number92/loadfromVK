from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField

ADVERTISING_AGENCY_OFFICE = 'agency_office'
USER_ACCOUNT = 'user_account'


class Cabinet(models.Model):
    """Рекламный кабинет"""
    CABINET_TYPE = (
        (ADVERTISING_AGENCY_OFFICE, 'Кабинет рекламного агенства'),
        (USER_ACCOUNT, 'Кабинет пользователя')
    )
    number = models.CharField(max_length=settings.LEN_ID_CABINET, blank=False)
    parametr = models.CharField(choices=CABINET_TYPE)
    id_app = models.CharField(
        settings.LEN_ID_APP,
        blank=False)


class Adversiting_campaign(models.Model):
    name = models.CharField(max_length=30, blank=False)
    campaign_id = models.CharField(max_length=30, blank=False)


class Advertisement(models.Model):
    campaign = models.ForeignKey(
        Adversiting_campaign,
        on_delete=models.CASCADE,
        related_name='advertiements')   
    ad_id = models.CharField(max_length=30, blank=False)
    impressions = models.CharField(max_length=30, blank=True)
    clicks = models.CharField(max_length=30, blank=True)
    spent = models.CharField(max_length=30, blank=True)
    date = models.DateField()


class Client(models.Model):
    """Клиент"""
    id_client = models.CharField(
        max_length=settings.LEN_ID_CABINET,
        blank=False)
    cabinet = models.ForeignKey(
        Cabinet,
        on_delete=models.CASCADE,
        related_name='client'
    )


class User(AbstractUser):
    """Класс пользователей."""

    phone_number = PhoneNumberField(blank=False)
    email = models.EmailField(
        max_length=settings.EMAIL_LENGTH,
        verbose_name='Email',
        unique=True,
        blank=False
    )
    first_name = models.CharField(
        max_length=settings.FIRST_NAME_LENGTH,
        verbose_name='Имя',
        blank=True
    )
    last_name = models.CharField(
        max_length=settings.LAST_NAME_LENGTH,
        verbose_name='Фамилия',
        blank=True
    )
    cabinet = models.ForeignKey(
        Cabinet,
        on_delete=models.CASCADE,
        verbose_name='Кабинет'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('last_name',)

    def __str__(self):
        return self.first_name





