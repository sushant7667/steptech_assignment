# Generated by Django 4.2.3 on 2023-07-24 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_backend', '0002_addus_isactive'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='addus',
            new_name='User',
        ),
    ]
