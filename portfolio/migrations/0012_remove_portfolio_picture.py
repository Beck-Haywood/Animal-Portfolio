# Generated by Django 2.2.6 on 2019-12-12 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='picture',
        ),
    ]
