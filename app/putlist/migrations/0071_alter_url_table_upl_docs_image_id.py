# Generated by Django 3.2.18 on 2023-04-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0070_auto_20230404_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='UPL_DOCS_IMAGE_ID',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='putlist/', verbose_name='Образ подписанного путевого листа'),
        ),
    ]
