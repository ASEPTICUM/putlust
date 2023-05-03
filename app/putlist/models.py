from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

# Create your models here.


unique_id = uuid.uuid4().hex

OPEN = 'Открытый'
LOCK = 'Закрытый'


##ПУТЕВОЙ ЛИСТ
class URL_TABLE(models.Model):
    status = (
        (OPEN, 'Открытый'),
        (LOCK, 'Закрытый'),
    )   
    id = models.AutoField(primary_key=True, db_index=True)
    #NAME = models.CharField(max_length=255, verbose_name='Название')
    PL_DATE = models.DateTimeField( verbose_name='Дата документа')
    SPR_USER_FIN_ID = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, verbose_name='Пользователь создавший запись')
    
    UPL_DOCS_IMAGE_ID = models.ImageField(null=True, blank=True, max_length=255, upload_to="putlist/", verbose_name='Образ подписанного путевого листа')
    
    REG_DATE = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')

    SROK_DEISTV = models.DateTimeField(verbose_name='Действительный до') 
    
    SPR_ORG_ID = models.ForeignKey('SPR_ORG', on_delete=models.PROTECT, verbose_name='Организация', default=1)#связь "ОРГАНИЗАЦИЯ"
    SPR_AUTO_ID = models.ForeignKey('SPR_AUTO', on_delete=models.PROTECT, verbose_name='Автомобиль', default=1)#связь "АВТОМОБИЛИ"
    SPR_DRIVER_ID = models.ForeignKey('SPR_DRIVER', on_delete=models.PROTECT, verbose_name='Водитель', default=1)#связь "ВОДИТЕЛИ"
    SPR_MARK_TOPL_ID = models.ForeignKey('SPR_MARK_TOPL', on_delete=models.PROTECT, verbose_name='Марка топлива', default=1)#связь "ТОПЛИВА"
    SPR_REZHIM_ID = models.ForeignKey('SPR_REZHIM', on_delete=models.PROTECT,verbose_name='Режим работы', default=1)#связь "РЕЖИМ РАБОТЫ"

    VYIEZD_SPEEDOMETER = models.IntegerField(verbose_name='Показания спидометра при выезде')
    VYIEZD_TIME = models.DateTimeField(null=True, blank=True, verbose_name='Время выезда фактическое, д/м/г м/ч') 
    VOZVR_SPEEDOMETER = models.IntegerField(null=True, blank=True, verbose_name='Показания спидометра по возваращению')
    VOZVR_TIME = models.DateTimeField(null=True, blank=True, verbose_name='Время возвращения фактическое д/м/г м/ч') 
    DG_VYIDANO = models.IntegerField(null=True, blank=True, verbose_name='Движение горючего выдано')
    DG_OST_VYIEZD = models.IntegerField(verbose_name='Движение горючего остаток горючего при выезде')
    DG_OST_VOZVR = models.IntegerField(null=True, blank=True, verbose_name='Движение горючего остаток горючего при возвращении')
    VR_SPECOB = models.CharField(null=True, blank=True, max_length=15, verbose_name='Время работы спецоборудования')
    VR_DVIG = models.CharField(max_length=15, null=True, blank=True, verbose_name='Время работы двигателя')

   
    
    DATE_DOP = models.DateTimeField(null=True, blank=True, verbose_name='Дата допуска водителя по состоянию здоровья.') 
    DATE_CONTROL = models.DateTimeField(verbose_name='Предрейсовый контроль ТС прошел. ')
    FIO_MEH = models.CharField(max_length=200, verbose_name='ФИО механика')
    FIO_MEH_PRIN = models.CharField(max_length=200, verbose_name='ФИО принявшего механика')
    KOLONNA = models.CharField(max_length=5, null=True, blank=True, verbose_name='Колонна')
    BRIGADA =models.CharField(max_length=5, null=True, blank=True, verbose_name='Бригада')
    FIO_DISP = models.CharField(max_length=200, verbose_name='ФИО диспетчера')
    SPR_SER_ID = models.ForeignKey('SPR_SER', on_delete=models.PROTECT, verbose_name='Код серии документа')

    PROBEG = models.IntegerField(null=True, blank=True, verbose_name='Пробег')
    RASHOD = models.IntegerField(null=True, blank=True, verbose_name='Расход')

    STATUS = models.CharField(max_length=255, null=True, blank=True, choices=status)

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):      
        if self.VOZVR_SPEEDOMETER != None:
            self.PROBEG = self.VOZVR_SPEEDOMETER - self.VYIEZD_SPEEDOMETER
        if self.DG_OST_VOZVR != None:
            self.RASHOD = self.DG_OST_VYIEZD + self.DG_VYIDANO - self.DG_OST_VOZVR
        if self.DG_OST_VOZVR == None:
            self.STATUS = OPEN
        else:
            self.STATUS = LOCK
        super().save(*args, **kwargs) 

    class Meta:
        managed = True
        db_table = 'put_list'
        verbose_name = "Путевой лист"
        ordering = ['-REG_DATE']


        
    
class ZAKAZ(models.Model):
    UPL_TABLE_ID = models.ForeignKey(URL_TABLE, on_delete=models.CASCADE, default=None, blank=True)
    ZAKAZCHIK = models.CharField(max_length=100, verbose_name='В чье распоряжение (наименование и адрес заказчика)')
    TIME_PRIB = models.CharField(max_length=5, verbose_name='Время прибытия')
    TIME_UB = models.CharField(max_length=5, verbose_name='Время убытия')
    TYPE_WORK = models.CharField(max_length=50, verbose_name='Вид работы')
    COMMENTS = models.CharField(null=True, blank=True, max_length=50, verbose_name='Особые отметки')
    
    def __str__(self):
        return str(self.ZAKAZCHIK)
    
    class Meta:
        db_table = 'zakaz'
        verbose_name = "Заказчики"
        verbose_name_plural = "Заказчики"  
    

    #def clean_date(self):
       # PL_DATE = self.cleaned_data['PL_DATE']
        #if PL_DATE < datetime.date.today():
          #  raise models.ValidationError("The date cannot be in the past!")
        #return PL_DATE



class SPR_AUTO(models.Model):
    GOS_NUM = models.CharField(max_length=255, db_index=True, verbose_name='Гос.номер')
    MARK = models.CharField(max_length=255, verbose_name='Марка автомобиля')

    def __str__(self):
        return self.MARK
    
    class Meta:
        verbose_name = "Автомобили"
        verbose_name_plural = "Автомобили"
        


class SPR_DRIVER(models.Model):
    FIO = models.CharField(max_length=100, db_index=True, verbose_name='ФИО Водителя полностью')
    NAME = models.CharField(max_length=300, verbose_name='ФИО Водителя сокращенно')
    TN = models.IntegerField(verbose_name='Табельный номер')
    UD_NUMBER = models.CharField(max_length=20, verbose_name='Номер Удостоверения')


    def __str__(self):
        return self.FIO
    
    class Meta:
        verbose_name = "Водители"
        verbose_name_plural = "Водители"



class SPR_MARK_TOPL(models.Model):
    NAME = models.CharField(max_length=10, db_index=True, verbose_name='Название Марки топлива')

    def __str__(self):
        return self.NAME
    
    class Meta:
        verbose_name = "Марка топлива"
        verbose_name_plural = "Марка топлива"



class SPR_ORG(models.Model):
    NAME = models.CharField(max_length=1024, db_index=True, verbose_name='Наименования Организации')
    SHTAMP = models.CharField(max_length=1024, verbose_name='Штамп организации (левый верхний угол)')

    def __str__(self):
        return self.NAME
    
    class Meta:
        verbose_name = "Организации"
        verbose_name_plural = "Организации"



class SPR_REZHIM(models.Model):
    NAME = models.CharField(max_length=30, db_index=True, verbose_name='Наименование Режима работы')
    TIME_VYIEZD = models.CharField(max_length=8, verbose_name='Время по графику - выезд из гаража')
    TIME_VOZVR = models.CharField(max_length=8, verbose_name='Время по графику - возвращение в гараж')

    def __str__(self):
        return self.NAME
    
    class Meta:
        verbose_name = "Режим работы"
        verbose_name_plural = "Режим работы"



class SPR_SER(models.Model):
    SPR_ORG_ID = models.IntegerField(db_index=True, verbose_name='Код Организации')
    NEXT_PL_NUMBER = models.IntegerField(verbose_name='Следующий номер документа')
    SER = models.CharField(max_length=20, verbose_name='Серия документа')

    def __str__(self):
        return self.SER
    
    class Meta:
        verbose_name = "Серия Путевых листов"
        verbose_name_plural = "Серия Путевых листов"












    
        
        
        
        
        



