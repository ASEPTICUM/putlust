# Generated by Django 3.2.18 on 2023-03-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0026_alter_spr_driver_fio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='REG_DATE',
            field=models.DateTimeField(verbose_name='Дата создания записи'),
        ),
    ]
