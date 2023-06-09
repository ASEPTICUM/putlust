# Generated by Django 3.2.18 on 2023-03-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0020_auto_20230313_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='PL_NUMBER',
            field=models.IntegerField(verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='UPL_DOCS_IMAGE_ID',
            field=models.IntegerField(verbose_name='Код образа подписанного путевого листа'),
        ),
    ]
