from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):

    def handle(self, *args, **options):
        # create or update curator_demo user
        user, created = User.objects.get_or_create(
            username='curator_demo',
            defaults={
                'is_staff': False,
                'is_superuser': False,
                'is_active': True,
            }
        )
        user.set_password('P4ace_CHASer')
        user.save()
        
        # create or get curator group
        curator_group, _ = Group.objects.get_or_create(name='Curator')
        user.groups.add(curator_group)
        
        # creat or update Aadmin user
        admin, created = User.objects.get_or_create(
            username='Admin',
            defaults={
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            }
        )
        admin.set_password('Ric3Sh0wer')
        admin.save()
        admin.groups.add(curator_group)
        
        self.stdout.write(self.style.SUCCESS('Demo users created/updated:'))
        self.stdout.write(f'  curator_demo / P4ace_CHASer')
        self.stdout.write(f'  Admin / Ric3Sh0wer')