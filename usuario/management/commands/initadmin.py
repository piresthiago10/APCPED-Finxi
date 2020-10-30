from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        print(User.objects.count())
        if User.objects.count() == 0:
            admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('A conta só será criada se não houver uma conta de adminstrador.')