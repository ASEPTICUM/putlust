# Generated by Django 3.2.18 on 2023-03-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putlist', '0009_auto_20230313_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPR_AUTO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GOS_NUM', models.CharField(max_length=255, verbose_name='Гос.номер')),
                ('MARK', models.CharField(max_length=255, verbose_name='Марка автомобиля')),
            ],
            options={
                'verbose_name': 'Автомобили',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='SPR_DRIVER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=100, verbose_name='Гос.номер')),
                ('NAME', models.CharField(max_length=300, verbose_name='ФИО Водителя сокращенно')),
                ('TN', models.IntegerField(verbose_name='Табельный номер')),
                ('UD_NUMBER', models.CharField(max_length=20, verbose_name='Номер Удостоверения')),
            ],
            options={
                'verbose_name': 'Водители',
                'verbose_name_plural': 'Водители',
            },
        ),
        migrations.CreateModel(
            name='SPR_MARK_TOPL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=10, verbose_name='Название Марки топлива')),
            ],
            options={
                'verbose_name': 'Марка топлева',
                'verbose_name_plural': 'Марка топлева',
            },
        ),
        migrations.CreateModel(
            name='SPR_ORG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=600, verbose_name='Наименования Организации')),
                ('SHTAMP', models.CharField(max_length=600, verbose_name='Штамп организации (левый верхний угол)')),
            ],
            options={
                'verbose_name': 'Организации',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='SPR_REZHIM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=30, verbose_name='Наименование Режима работы')),
                ('TIME_VYIEZD', models.CharField(max_length=8, verbose_name='Время по графику - выезд из гаража')),
                ('TIME_VOZVR', models.CharField(max_length=8, verbose_name='Время по графику - возвращение в гараж')),
            ],
            options={
                'verbose_name': 'Режим работы',
                'verbose_name_plural': 'Режим работы',
            },
        ),
        migrations.CreateModel(
            name='SPR_SER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SPR_ORG_ID', models.IntegerField(verbose_name='Код Организации')),
                ('NEXT_PL_NUMBER', models.IntegerField(verbose_name='Следующий номер документа')),
                ('SER', models.CharField(max_length=20, verbose_name='Серия документа')),
            ],
            options={
                'verbose_name': 'Серия Путевых листов',
                'verbose_name_plural': 'Серия Путевых листов',
            },
        ),
        migrations.CreateModel(
            name='ZAKAZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZAKAZCHIK', models.CharField(max_length=100, verbose_name='В чье распоряжение (наименование и адрес заказчика)')),
                ('TIME_PRIB', models.CharField(max_length=5, verbose_name='Время прибытия')),
                ('TIME_UB', models.CharField(max_length=5, verbose_name='Время убытия')),
                ('TYPE_WORK', models.CharField(max_length=50, verbose_name='Вид работы')),
                ('COMMENTS', models.CharField(max_length=50, verbose_name='Особые отметки')),
                ('UPL_TABLE_ID', models.IntegerField(verbose_name='Номер записи Путевого листа')),
                ('Z_NUM', models.IntegerField(verbose_name='Номер записи')),
            ],
            options={
                'verbose_name': 'Заказчики',
                'verbose_name_plural': 'Заказчики',
            },
        ),
        migrations.AlterField(
            model_name='url_table',
            name='BRIGADA',
            field=models.CharField(max_length=5, verbose_name='Бригада'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='DG_OST_VOZVR',
            field=models.IntegerField(verbose_name='Движение горючего остаток горючего при возвращении'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='DG_OST_VYIEZD',
            field=models.IntegerField(verbose_name='Движение горючего остаток горючего при выезде'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='DG_VYIDANO',
            field=models.IntegerField(verbose_name='Движение горючего выдано'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='FIO_DISP',
            field=models.CharField(max_length=200, verbose_name='ФИО диспетчера'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='FIO_MEH',
            field=models.CharField(max_length=200, verbose_name='ФИО механика'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='FIO_MEH_PRIN',
            field=models.CharField(max_length=200, verbose_name='ФИО принявшего механика'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='KOLONNA',
            field=models.CharField(max_length=5, verbose_name='Колонна'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='PL_NUMBER',
            field=models.IntegerField(verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_AUTO_ID',
            field=models.IntegerField(verbose_name='Код автомобиля'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_DRIVER_ID',
            field=models.IntegerField(verbose_name='Код водителя'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_MARK_TOPL_ID',
            field=models.IntegerField(verbose_name='Код марки топлива'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_ORG_ID',
            field=models.IntegerField(verbose_name='Код организации'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_REZHIM_ID',
            field=models.IntegerField(verbose_name='Код режима работы'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='SPR_SER_ID',
            field=models.IntegerField(verbose_name='Код серии документа'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='TIME_PRIB',
            field=models.CharField(max_length=15, verbose_name='Время прибытия'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='TIME_UB',
            field=models.CharField(max_length=15, verbose_name='Время убытия'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='TYPE_WORK',
            field=models.CharField(max_length=50, verbose_name='Вид работы'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='UPL_DOCS_IMAGE_ID',
            field=models.IntegerField(verbose_name='Код образа подписанного путевого листа'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VOZVR_SPEEDOMETER',
            field=models.IntegerField(verbose_name='Показания спидометра по возваращению'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VR_DVIG',
            field=models.CharField(max_length=15, verbose_name='Время работы двигателя'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VR_SPECOB',
            field=models.CharField(max_length=15, verbose_name='Время работы спецоборудования'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='VYIEZD_SPEEDOMETER',
            field=models.IntegerField(verbose_name='Показания спидометра при выезде'),
        ),
        migrations.AlterField(
            model_name='url_table',
            name='ZAKAZCHIK',
            field=models.CharField(max_length=100, verbose_name='В чье распоряжение'),
        ),
    ]