from django.db import models


class Participants(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    district_id = models.IntegerField(default=41)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name} - {self.email}'
