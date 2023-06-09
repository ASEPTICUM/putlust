# Generated by Django 3.2.18 on 2023-03-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0027_alter_url_table_reg_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spr_org',
            name='NAME',
            field=models.CharField(db_index=True, max_length=1024, verbose_name='Наименования Организации'),
        ),
        migrations.AlterField(
            model_name='spr_org',
            name='SHTAMP',
            field=models.CharField(max_length=1024, verbose_name='Штамп организации (левый верхний угол)'),
        ),
    ]
