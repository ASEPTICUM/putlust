# Generated by Django 3.2.18 on 2023-03-28 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0057_auto_20230328_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakaz',
            name='UPL_TABLE_ID',
            field=models.ForeignKey(blank=True, default='e6d4b6f609eb4f6faee92fe04f7967ad', on_delete=django.db.models.deletion.CASCADE, to='putlist.url_table'),
        ),
    ]
