# Generated by Django 3.2.18 on 2023-04-11 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0087_alter_url_table_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url_table',
            options={'managed': True, 'ordering': ['-STATUS'], 'verbose_name': 'Путевой лист'},
        ),
    ]