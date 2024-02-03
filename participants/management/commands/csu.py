from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="dsgov").exists():
            user = User.objects.create(
                username="dsgov",
                first_name="Elon",
                last_name="Mask",
                is_superuser=True,
                is_staff=True,
                is_active=True,
            )

            user.set_password("!Vjlxfybt45")
            user.save()
