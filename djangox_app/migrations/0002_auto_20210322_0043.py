# Generated by Django 3.1.7 on 2021-03-22 00:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangox_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Djangox',
            new_name='Person',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='puchaser',
            new_name='profile_manager',
        ),
    ]
