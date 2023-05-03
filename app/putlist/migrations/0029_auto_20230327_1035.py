# Generated by Django 3.2.18 on 2023-03-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0028_auto_20230327_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='VOZVR_SPEEDOMETER',
            field=models.IntegerField(blank=True, null=True, verbose_name='Показания спидометра по возваращению'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VOZVR_TIME',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время возвращения фактическое д/м/г м/ч'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VR_DVIG',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Время работы двигателя'),
        ),
    ]