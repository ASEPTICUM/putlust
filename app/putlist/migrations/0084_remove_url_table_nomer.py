# Generated by Django 3.2.18 on 2023-04-11 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0083_url_table_nomer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url_table',
            name='nomer',
        ),
    ]
