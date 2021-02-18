# Generated by Django 3.1.4 on 2021-02-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0006_auto_20210210_2044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='raport',
            options={'ordering': ('-created', '-shift')},
        ),
        migrations.AlterField(
            model_name='raport',
            name='team',
            field=models.CharField(choices=[('1', 'Team_1'), ('2', 'Team_2'), ('3', 'Team_3'), ('4', 'Team_4')], default='t1', max_length=10),
        ),
    ]