# Generated by Django 4.2 on 2023-05-02 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalwis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='close_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 21, 5, 15, 974125, tzinfo=datetime.timezone.utc)),
        ),
    ]
