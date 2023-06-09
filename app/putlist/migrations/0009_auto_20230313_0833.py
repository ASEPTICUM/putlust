# Generated by Django 3.2.18 on 2023-03-13 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('putlist', '0008_alter_url_table_pl_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='BRIGADA',
            field=models.CharField(max_length=25, verbose_name='Бригада'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='DATE_CONTROL',
            field=models.DateTimeField(verbose_name='Предрейсовый контроль ТС прошел. '),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='DATE_DOP',
            field=models.DateTimeField(verbose_name='Дата допуска водителя по состоянию здоровья.'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='DG_OST_VOZVR',
            field=models.IntegerField(max_length=255, verbose_name='Движение горючего остаток горючего при возвращении'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='DG_OST_VYIEZD',
            field=models.IntegerField(max_length=255, verbose_name='Движение горючего остаток горючего при выезде'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='DG_VYIDANO',
            field=models.IntegerField(max_length=255, verbose_name='Движение горючего выдано'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='FIO_DISP',
            field=models.CharField(max_length=25, verbose_name='ФИО диспетчера'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='FIO_MEH',
            field=models.CharField(max_length=25, verbose_name='ФИО механика'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='FIO_MEH_PRIN',
            field=models.CharField(max_length=25, verbose_name='ФИО принявшего механика'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='KOLONNA',
            field=models.CharField(max_length=25, verbose_name='Колонна'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='PL_NUMBER',
            field=models.IntegerField(max_length=255, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='REG_DATE',
            field=models.DateTimeField(verbose_name='Дата  создания записи'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_AUTO_ID',
            field=models.IntegerField(max_length=255, verbose_name='Код автомобиля'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_DRIVER_ID',
            field=models.IntegerField(max_length=255, verbose_name='Код водителя'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_MARK_TOPL_ID',
            field=models.IntegerField(max_length=255, verbose_name='Код марки топлива'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_ORG_ID',
            field=models.IntegerField(max_length=255, verbose_name='Код организации'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_REZHIM_ID',
            field=models.IntegerField(max_length=255, verbose_name='Код режима работы'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_SER_ID',
            field=models.IntegerField(max_length=255, verbose_name='Код серии документа'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_USER_FIN_ID',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь создавший запись'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SROK_DEISTV',
            field=models.DateTimeField(verbose_name='Действительный до'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='TIME_PRIB',
            field=models.CharField(max_length=255, verbose_name='Время прибытия'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='TIME_UB',
            field=models.CharField(max_length=255, verbose_name='Время убытия'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='TYPE_WORK',
            field=models.CharField(max_length=255, verbose_name='Вид работы'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='UPL_DOCS_IMAGE_ID',
            field=models.IntegerField(max_length=255, verbose_name='Код образа подписанного путевого листа'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VOZVR_SPEEDOMETER',
            field=models.IntegerField(max_length=255, verbose_name='Показания спидометра по возваращению'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VOZVR_TIME',
            field=models.DateTimeField(verbose_name='Время возвращения фактическое д/м/г м/ч'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VR_DVIG',
            field=models.CharField(max_length=255, verbose_name='Время работы двигателя'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VR_SPECOB',
            field=models.CharField(max_length=255, verbose_name='Время работы спецоборудования'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VYIEZD_SPEEDOMETER',
            field=models.IntegerField(max_length=255, verbose_name='Показания спидометра при выезде'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VYIEZD_TIME',
            field=models.DateTimeField(verbose_name='Время выезда фактическое, д/м/г м/ч'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='ZAKAZCHIK',
            field=models.CharField(max_length=255, verbose_name='В чье распоряжение'),
        ),
    ]
