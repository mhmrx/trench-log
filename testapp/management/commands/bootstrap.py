from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('migrate', interactive=False)

        if not User.objects.first():
            u = User(
                username='admin',
                email='admin@django-trench.com',
                is_staff=True,
                is_superuser=True,
            )
            u.set_password('q1w2e3r4')
            u.save()
