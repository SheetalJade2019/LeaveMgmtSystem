# Generated by Django 3.0.8 on 2020-09-22 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leavedata',
            old_name='status',
            new_name='leave_status',
        ),
    ]
