# Generated by Django 3.2.18 on 2023-05-03 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0093_alter_url_table_upl_docs_image_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url_table',
            options={'managed': True, 'ordering': ['-PL_DATE'], 'verbose_name': 'Путевой лист'},
        ),
        migrations.RemoveField(
            model_name='url_table',
            name='date',
        ),
        migrations.AlterField(
            model_name='url_table',
            name='PL_DATE',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата документа'),
        ),
    ]
