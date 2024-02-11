# Participants API

Проект представляет собой backend приложения, предназначенного для работы с регистрацией участников квиза.

## Оглавление

- [Технологии](#технологии)
- [Описание](#описание)
- [Настройка](#настройка)
- [Установка](#установка)


## Технологии

- [![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/) [![Django Rest Framework](https://img.shields.io/badge/-Django_Rest_Framework-092E20?style=flat)](https://www.django-rest-framework.org/)
- [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
- [![Gunicorn](https://img.shields.io/badge/-Gunicorn-589636?style=flat&logo=gunicorn&logoColor=white)](https://gunicorn.org/) [![NGINX](https://img.shields.io/badge/-NGINX-269539?style=flat&logo=nginx&logoColor=white)](https://www.nginx.com/)
- [![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

## Описание

Participants API разработан для управления данными зарегистрированных участников. Проект представляет API эндпоинт для
регистрации
участников, а также позволяем управлять данными через административный интерфейс Django.

Изначальное ТЗ было представлено разработкой API эндпоинта для регистрации данных участника квиза, в процессе разработки
были добавлены дополнительные функции представленные в виде камстомных действий в админке Django, такие как отправка
данных на сторонний
API, выгрузка данных в форматах CSV и Excel.

## Настройка

- Для начала работы с проектом клонируйте репозиторий:
    - ```git clone https://github.com/NickolayBabulich/participants_api.git```
- Отредактируйте файл .env.sample указав ваши данные (логины, названия, пароли, домен), все заполненные данные в файле
  приведены для
  примера.
- После редактирования файла .env.sample переименуйте файл в .env
- В папке nginx отредактируйте файл default.conf.sample, изменив server_name example.ru на ваше доменное имя, после
  переименуйте в default.conf

## Установка
- В данной конфигурации проект готов к деплою с использованием docker
