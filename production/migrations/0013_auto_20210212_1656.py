# Generated by Django 3.1.4 on 2021-02-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0012_auto_20210212_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday_request',
            name='date_begin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='holiday_request',
            name='date_end',
            field=models.DateField(),
        ),
    ]
