# Generated by Django 3.2.18 on 2023-03-28 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0037_auto_20230328_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='ZADAN',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='putlist.zakaz'),
        ),
    ]
