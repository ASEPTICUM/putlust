# Generated by Django 3.2.18 on 2023-03-28 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0058_alter_zakaz_upl_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakaz',
            name='UPL_TABLE_ID',
            field=models.ForeignKey(blank=True, default='c2a50b43aeb44c5bb00f8d68b5dd03ab', on_delete=django.db.models.deletion.CASCADE, to='putlist.url_table'),
        ),
    ]
