from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.CharField("Роль", max_length=15, default='tourist')
    date_birth = models.DateTimeField(blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'role']

    def __str__(self):
        return self.username


class Trigger(models.Model):
    name = models.CharField(max_length=4096, blank=True, null=True, verbose_name="Название триггера")
    strict = models.BooleanField(blank=True, null=True, verbose_name="Строгий?")
    result = models.ManyToManyField('ResultOfTrigger', related_name="result_through_trigger", blank=True, null=True)


class ResultOfTrigger(models.Model):
    MEDIA_TYPE_CHOICES = [
        (1, 'text'),
        (2, 'picture'),
        (3, 'video'),
        (4, 'audio'),
        (5, 'gif'),
    ]
    result_of_trigger = models.CharField(max_length=4096, blank=True, null=True, verbose_name="Ответ Триггера")
    type_media = models.IntegerField(choices=MEDIA_TYPE_CHOICES, verbose_name='Квалификация', blank=True, null=True)
