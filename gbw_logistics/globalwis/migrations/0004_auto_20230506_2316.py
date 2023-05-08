# Generated by Django 3.2.16 on 2023-05-07 06:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('globalwis', '0003_auto_20230505_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='stations',
            name='close_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 7, 11, 16, 19, 899171, tzinfo=utc)),
        ),
    ]