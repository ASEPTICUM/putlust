# Generated by Django 3.2.18 on 2023-04-10 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0081_alter_url_table_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url_table',
            options={'managed': True, 'ordering': ['-STATUS'], 'verbose_name': 'Путевой лист'},
        ),
    ]
