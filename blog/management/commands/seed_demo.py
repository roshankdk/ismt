import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from blog.models import Category, Post


class Command(BaseCommand):
    help = 'Create a demo admin user and sample posts (safe to run many times).'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DEMO_ADMIN_USER')
        password = os.environ.get('DEMO_ADMIN_PASSWORD')

        if username and password:
            admin, created = User.objects.get_or_create(
                username=username, defaults={'is_staff': True, 'is_superuser': True}
            )
            if created:
                admin.set_password(password)
                admin.save()
            self.stdout.write(f'Admin user "{username}": {"created" if created else "already exists"}')
        else:
            admin = User.objects.filter(is_superuser=True).first()
            self.stdout.write('DEMO_ADMIN_USER / DEMO_ADMIN_PASSWORD not set: no admin created')

        if admin is None or Post.objects.exists():
            self.stdout.write('Sample posts skipped')
            return

        category, _ = Category.objects.get_or_create(name='Demo')
        for title in ('Welcome to the blog', 'Deployed by GitHub Actions', 'Third sample post'):
            Post.objects.create(
                title=title, author=admin, category=category,
                content=f'{title}. This sample post was added automatically when the site was deployed.',
            )
        self.stdout.write('Created 3 sample posts')
