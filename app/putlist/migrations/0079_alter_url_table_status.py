# Generated by Django 3.2.18 on 2023-04-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0078_url_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='STATUS',
            field=models.CharField(blank=True, choices=[('O', 'Открытый'), ('L', 'Закрытый')], max_length=255, null=True),
        ),
    ]