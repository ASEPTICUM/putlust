# Generated by Django 3.2.18 on 2023-03-28 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0036_url_table_zadan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url_table',
            options={'managed': True, 'verbose_name': 'Путевой лист'},
        ),
        migrations.AlterModelOptions(
            name='zakaz',
            options={'managed': True, 'verbose_name': 'Заказчики', 'verbose_name_plural': 'Заказчики'},
        ),
        migrations.AlterModelTable(
            name='url_table',
            table='put_list',
        ),
        migrations.AlterModelTable(
            name='zakaz',
            table='zakaz',
        ),
    ]