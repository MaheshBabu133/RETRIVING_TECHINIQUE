# Generated by Django 4.1.7 on 2023-04-07 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_actor_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actor_date',
            new_name='Actor_DOB',
        ),
    ]
