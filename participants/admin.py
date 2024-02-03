from django.contrib import admin
from participants.models import Participants


@admin.register(Participants)
class UserAuthAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Participants._meta.get_fields()]
    search_fields = ('first_name', 'second_name', 'phone')
