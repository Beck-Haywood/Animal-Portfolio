# Generated by Django 2.2.6 on 2019-12-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20191206_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
