# Generated by Django 2.2.4 on 2019-09-04 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_service_storage', '0002_auto_20190902_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]