from django import forms
from .models import URL_TABLE, SPR_AUTO, SPR_DRIVER, SPR_MARK_TOPL, SPR_ORG, SPR_REZHIM, SPR_SER, ZAKAZ
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.forms import ClearableFileInput


class FilterFormSer(forms.Form):
    ser = forms.ModelMultipleChoiceField(
        queryset=SPR_SER.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
class FilterFormOrg(forms.Form):
    org = forms.ModelMultipleChoiceField(
        queryset=SPR_ORG.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
class FilterFormAuto(forms.Form):
    auto = forms.ModelMultipleChoiceField(
        queryset=SPR_AUTO.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
class FilterFormDriver(forms.Form):
    driver = forms.ModelMultipleChoiceField(
        queryset=SPR_DRIVER.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
class FilterFormTopl(forms.Form):
    topl = forms.ModelMultipleChoiceField(
        queryset=SPR_MARK_TOPL.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class Put_List(forms.ModelForm):
    class Meta:
        model = URL_TABLE
        fields = '__all__'

    UPL_DOCS_IMAGE_ID = forms.ImageField(required=False)
    
    
    
    SPR_ORG_ID = forms.ModelChoiceField(queryset=SPR_ORG.objects.all(), empty_label="Не выбрано")
    SPR_AUTO_ID = forms.ModelChoiceField(queryset=SPR_AUTO.objects.all(), empty_label="Не выбрано")
    SPR_DRIVER_ID = forms.ModelChoiceField(queryset=SPR_DRIVER.objects.all(), empty_label="Не выбрано")
    SPR_MARK_TOPL_ID = forms.ModelChoiceField(queryset=SPR_MARK_TOPL.objects.all(), empty_label="Не выбрано")
    SPR_REZHIM_ID = forms.ModelChoiceField(queryset=SPR_REZHIM.objects.all(), empty_label="Не выбрано")

    PL_DATE = forms.DateTimeField(input_formats=['%d/%m/%Y'], widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    #REG_DATE = forms.DateTimeField(input_formats=['%d/%m/%Y'], widget=forms.DateTimeInput(attrs={
            #'class': 'form-control datetimepicker-input',
            #'data-target': '#datetimepicker2'
        #}))
    SROK_DEISTV = forms.DateTimeField(input_formats=['%d/%m/%Y'], widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker3'
        }))
    VYIEZD_TIME = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker4'
        }), required=False)
    VOZVR_TIME = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker5'
        }), required=False)
    DATE_DOP = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker6'
        }), required=False)  
    DATE_CONTROL = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker7'
        }))   
    

    VOZVR_SPEEDOMETER = forms.IntegerField(required=False)
    VR_DVIG = forms.CharField(required=False)
    DG_VYIDANO = forms.IntegerField(required=False)
    KOLONNA = forms.CharField(required=False)
    BRIGADA =forms.CharField(required=False)
    VR_SPECOB = forms.CharField(required=False)
    DG_OST_VOZVR = forms.IntegerField(required=False)



class Automob(forms.ModelForm):
    class Meta:
        model = SPR_AUTO
        fields = ['GOS_NUM','MARK']

class Drivers(forms.ModelForm):
    class Meta:
        model = SPR_DRIVER
        fields = ['FIO','NAME','TN','UD_NUMBER']

class MarkToplivo(forms.ModelForm):
    class Meta:
        model = SPR_MARK_TOPL
        fields = ['NAME']

class Organozations(forms.ModelForm):
    class Meta:
        model = SPR_ORG
        fields = ['NAME','SHTAMP']

class TimeWork(forms.ModelForm):
    class Meta:
        model = SPR_REZHIM
        fields = ['NAME','TIME_VYIEZD','TIME_VOZVR']

class SeriaList(forms.ModelForm):
    class Meta:
        model = SPR_SER
        fields = ['SPR_ORG_ID','NEXT_PL_NUMBER','SER']

class Zakazchiki(forms.ModelForm):       
    def __init__(self, pk):
        if (pk.__class__ != int):
            super(Zakazchiki, self).__init__(pk)
            return
        super(Zakazchiki, self).__init__()
        self.fields['UPL_TABLE_ID'] = forms.IntegerField(initial=URL_TABLE.objects.values_list("id").get(pk=pk)[0])
    
    
    class Meta:
        model = ZAKAZ
        fields = ['ZAKAZCHIK','TIME_PRIB','TIME_UB','TYPE_WORK','COMMENTS','UPL_TABLE_ID']
        
        
        
    
        
    
    

    


    

    
