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

    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name} - {self.email}'


class TestSending(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    district_id = models.IntegerField(default=41)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.email}'


class Log(models.Model):
    status_answer = [
        ('accepted', 'Успешно отправлено'),
        ('rejected', 'Ошибка отправки')
    ]

    user_id = models.IntegerField()
    email = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=25, choices=status_answer)
    server_response = models.CharField(max_length=100)
    timestamp = models.DateTimeField(blank=True, null=True)
