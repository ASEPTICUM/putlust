# Generated by Django 3.2.18 on 2023-05-03 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0096_alter_url_table_dg_vyidano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='DATE_DOP',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата допуска водителя по состоянию здоровья.'),
        ),
    ]
