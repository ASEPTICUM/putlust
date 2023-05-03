# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
#from .models import URL_TABLE, SPR_AUTO, SPR_DRIVER, SPR_MARK_TOPL, SPR_ORG, SPR_REZHIM, SPR_SER, ZAKAZ
#from .forms import Put_List, Automob, Drivers, MarkToplivo, Organozations, SeriaList, Zakazchiki, TimeWork, FilterFormSer, FilterFormOrg, FilterFormAuto
from .forms import *
from .models import *
from django.views.generic import UpdateView, DeleteView, ListView, View
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.files.storage import FileSystemStorage
import json
from django.urls import reverse
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas
import reportlab
import reportlab.rl_config
from reportlab.pdfbase.ttfonts import TTFont
from django.core.paginator import Paginator
from django.conf import settings
import os
import io
from docx import Document
from docxtpl import DocxTemplate
from django.db.models import Sum
# Create your views here.




def render_pdf_view(request, pk):
    date = URL_TABLE.objects.get(id=pk)
    context = {'putlist': date}

    template_path = os.path.join(settings.BASE_DIR, 'templates', 'putlist/my_template.docx')
    template = DocxTemplate(template_path)
    
    template.render(context)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename=my_template"{date.id}".docx'

    doc_stream = io.BytesIO()
    template.save(doc_stream)
    doc_stream.seek(0)
    response.write(doc_stream.getvalue())
    
    return response




#deletes  
class Delete(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        URL_TABLE.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }  
        return JsonResponse(data)

class NewDelete2(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        SPR_AUTO.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }  
        return JsonResponse(data)
    
class Delete4(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        ZAKAZ.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }  
        return JsonResponse(data)

class NewDelete3(View):   
    def get(self, request):
        id1 = request.GET.get('id', None)
        SPR_DRIVER.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }  
        return JsonResponse(data)
    
class NewDelete5(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        SPR_MARK_TOPL.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }  
        return JsonResponse(data)
    
class NewDelete7(View): 
    def get(self, request):
        id1 = request.GET.get('id', None)
        SPR_REZHIM.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }  
        return JsonResponse(data)
    
class NewDelete6(DeleteView): 
    def get(self, request):
        id1 = request.GET.get('id', None)
        SPR_ORG.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }  
        return JsonResponse(data)
    
class NewDelete8(DeleteView):   
    def get(self, request):
        id1 = request.GET.get('id', None)
        SPR_SER.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }  
        return JsonResponse(data)


#updates

#напиши функцию обновление данных в записи через форму не используя класс UpdateView
    


def NewUpdate(request, pk):
    zakazz = ZAKAZ.objects.filter(UPL_TABLE_ID=pk) ##передовать записи с определённым id, условие: id zakaz == id put_list
    put_list = URL_TABLE.objects.get(pk=pk)
    if request.method == 'POST':
        form = Put_List(request.POST, request.FILES, instance=put_list)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    else:
        form = Put_List(instance=put_list)
    obj = URL_TABLE.objects.get(pk=pk)      
    return TemplateResponse(request, 'putlist/forms/Form_index.html', {'form': form,  'zakazs': zakazz, 'obj': obj})


class NewUpdate2(UpdateView):
    model = SPR_AUTO
    template_name = 'putlist/car.html'
    success_url = '/car'
    fields = ['GOS_NUM','MARK']    



def second(request):
    objs = URL_TABLE.objects.latest('id')
    return render(request, 'putlist/forms/second.html', {'obj': objs})


def spravochniki(request):
    return render(request, 'putlist/spravoch.html')



def index(request):
    search = request.GET.get('q', '')
    form = FilterFormSer(request.POST)
    formTwo = FilterFormOrg(request.POST)
    formThree = FilterFormAuto(request.POST)
    formFour = FilterFormDriver(request.POST)
    formFive = FilterFormTopl(request.POST)
    putlist = URL_TABLE.objects.all()
    countNomer = URL_TABLE.objects.all().count()
    countFire = URL_TABLE.objects.aggregate(Sum('RASHOD'))['RASHOD__sum']
    has_checkbox_sort = False
      
    if search:
        putlist = putlist.filter(
            Q(STATUS__icontains=search) |
            Q(id__icontains=search) | 
            Q(SPR_SER_ID__SER__icontains=search) |
            Q(PL_DATE__icontains=search) |
            Q(DG_VYIDANO__icontains=search) |
            Q(DG_OST_VYIEZD__icontains=search)|
            Q(DG_OST_VOZVR__icontains=search)|
            Q(SPR_AUTO_ID__MARK__icontains=search)|
            Q(SPR_ORG_ID__NAME__icontains=search)|
            Q(SPR_DRIVER_ID__FIO__icontains=search)|
            Q(SPR_MARK_TOPL_ID__NAME__icontains=search)|
            Q(RASHOD__icontains=search)|
            Q(PROBEG__icontains=search)|
            Q(SPR_AUTO_ID__GOS_NUM__icontains=search))
        countNomer = putlist.filter(
            Q(STATUS__icontains=search) |
            Q(id__icontains=search) | 
            Q(SPR_SER_ID__SER__icontains=search) |
            Q(PL_DATE__icontains=search) |
            Q(DG_VYIDANO__icontains=search) |
            Q(DG_OST_VYIEZD__icontains=search)|
            Q(DG_OST_VOZVR__icontains=search)|
            Q(SPR_AUTO_ID__MARK__icontains=search)|
            Q(SPR_ORG_ID__NAME__icontains=search)|
            Q(SPR_DRIVER_ID__FIO__icontains=search)|
            Q(SPR_MARK_TOPL_ID__NAME__icontains=search)|
            Q(RASHOD__icontains=search)|
            Q(PROBEG__icontains=search)|
            Q(SPR_AUTO_ID__GOS_NUM__icontains=search)).count()
        countFire = putlist.aggregate(Sum('RASHOD'))['RASHOD__sum']
        
    if form.is_valid():
        ser = form.cleaned_data['ser']
        putlist = URL_TABLE.objects.filter(SPR_SER_ID__in=ser)
        countNomer = URL_TABLE.objects.filter(SPR_SER_ID__in=ser).count()
        countFire = putlist.aggregate(Sum('RASHOD'))['RASHOD__sum']
        has_checkbox_sort = True
        
    if formTwo.is_valid():
        org = formTwo.cleaned_data['org']
        putlist = URL_TABLE.objects.filter(SPR_ORG_ID__in=org)
        countNomer = URL_TABLE.objects.filter(SPR_ORG_ID__in=org).count()
        countFire = putlist.aggregate(Sum('RASHOD'))['RASHOD__sum']
        has_checkbox_sort = True
        
    if formThree.is_valid():
        auto = formThree.cleaned_data['auto']
        putlist = URL_TABLE.objects.filter(SPR_AUTO_ID__in=auto)
        countNomer = URL_TABLE.objects.filter(SPR_AUTO_ID__in=auto).count()
        countFire = putlist.aggregate(Sum('RASHOD'))['RASHOD__sum']
        has_checkbox_sort = True
        
    if formFour.is_valid():
        driver = formFour.cleaned_data['driver']
        putlist = URL_TABLE.objects.filter(SPR_DRIVER_ID__in=driver)
        countNomer = URL_TABLE.objects.filter(SPR_DRIVER_ID__in=driver).count()
        countFire = putlist.aggregate(Sum('RASHOD'))['RASHOD__sum']
        has_checkbox_sort = True

    if formFive.is_valid():
        topl = formFive.cleaned_data['topl']
        putlist = URL_TABLE.objects.filter(SPR_MARK_TOPL_ID__in=topl)
        countNomer = URL_TABLE.objects.filter(SPR_MARK_TOPL_ID__in=topl).count()
        countFire = putlist.aggregate(Sum('RASHOD'))['RASHOD__sum']
        has_checkbox_sort = True


    paginator = Paginator(putlist, 11)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'putlists':putlist, 
        'page_obj':page_obj, 
        'form':form, 
        'formTwo':formTwo, 
        'formThree':formThree,
        'formFour':formFour,
        'formFive':formFive,
        'search':search,
        'has_checkbox_sort':has_checkbox_sort,
        'countNomer':countNomer,
        'countFire':countFire}

    return render(request, 'putlist/index.html', context)



def Form_index(request):
    form = Put_List(request.POST, request.FILES) if request.method == 'POST' else Put_List()
    if request.method == 'POST' and form.is_valid() and request.FILES:
        instance = form.save(commit=False)
        instance.SPR_USER_FIN_ID = request.user
        instance.save()
        return redirect('second')
    
    return render(request, 'putlist/forms/Form_index.html', {'form': form})

def Form_index_TWObtn(request):
    form = Put_List(request.POST, request.FILES) if request.method == 'POST' else Put_List()
    if request.method == 'POST' and form.is_valid() and request.FILES:
        instance = form.save(commit=False)
        instance.SPR_USER_FIN_ID = request.user
        instance.save()
        return redirect('/')
    
    return render(request, 'putlist/forms/Form_index.html', {'form': form})
    


def car(request):
    search = request.GET.get('q', '')
    car = SPR_AUTO.objects.all()

    if request.method == 'POST':
        form = Automob(request.POST) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.SPR_USER_FIN_ID = request.user
            instance.save()
            return redirect('car')
    else:
        form = Automob()

    if search:
        car = car.filter(
            Q(GOS_NUM__icontains=search) |
            Q(MARK__icontains=search))
    else:
        car = SPR_AUTO.objects.all()

    context = {
        'cars':car,
        'form':form, 
        'search':search,
        }
    return render(request, 'putlist/car.html', context)



def driver(request):
    search = request.GET.get('q', '')
    driver = SPR_DRIVER.objects.all()

    if request.method == 'POST':
        form = Drivers(request.POST) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.SPR_USER_FIN_ID = request.user
            instance.save()
            return redirect('driver')
    else:
        form = Drivers()

    if search:
        driver = driver.filter(
            Q(FIO__icontains=search) |
            Q(NAME__icontains=search)|
            Q(TN__icontains=search)|
            Q(UD_NUMBER__icontains=search))
    else:
        driver = SPR_DRIVER.objects.all()    

    context = {
        'drivers':driver,
        'form':form,
        'search':search,
    }
    
    return render(request, 'putlist/driver.html', context)


def toplivo(request):
    search = request.GET.get('q', '')
    toplivo = SPR_MARK_TOPL.objects.all()

    if request.method == 'POST':
        form = MarkToplivo(request.POST) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.SPR_USER_FIN_ID = request.user
            instance.save()
            return redirect('toplivo')
    else:
        form = MarkToplivo() 

    if search:
        toplivo = toplivo.filter(
            Q(NAME__icontains=search))
    else:
        toplivo = SPR_MARK_TOPL.objects.all()

    context = {
        'toplivos':toplivo,
        'form':form,
        'search':search,
    }

    return render(request, 'putlist/toplivo.html', context)


def timeWork(request):
    search = request.GET.get('q', '')
    timeWork = SPR_REZHIM.objects.all()

    if request.method == 'POST':
        form = TimeWork(request.POST) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.SPR_USER_FIN_ID = request.user
            instance.save()
            return redirect('timeWork')
    else:
        form = TimeWork()  

    if search:
        timeWork = timeWork.filter(
            Q(NAME__icontains=search)|
            Q(TIME_VYIEZD__icontains=search)|
            Q(TIME_VOZVR__icontains=search))
    else:
        timeWork = SPR_REZHIM.objects.all()

    context = {
        'timeWorks':timeWork,
        'form':form,
        'search':search,
    }

    return render(request, 'putlist/timeWork.html', context)


def organizations(request):
    search = request.GET.get('q', '')
    organizations = SPR_ORG.objects.all()

    if request.method == 'POST':
        form = Organozations(request.POST) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.SPR_USER_FIN_ID = request.user
            instance.save()
            return redirect('organizations')
    else:
        form = Organozations()  

    if search:
        organizations = organizations.filter(
            Q(NAME__icontains=search)|
            Q(SHTAMP__icontains=search))
    else:
        organizations = SPR_ORG.objects.all()

    context = {
        'organizationss':organizations, 
        'form':form,
        'search':search,
    }
   
    return render(request, 'putlist/organizations.html', context)


def series(request):
    search = request.GET.get('q', '')
    series = SPR_SER.objects.all()

    if request.method == 'POST':
        form = SeriaList(request.POST) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.SPR_USER_FIN_ID = request.user
            instance.save()
            return redirect('series')
    else:
        form = SeriaList() 

    if search:
        series = series.filter(
            Q(SPR_ORG_ID__icontains=search)|
            Q(NEXT_PL_NUMBER__icontains=search)|
            Q(SER__icontains=search))
    else:
        series = SPR_SER.objects.all()

    context = {
        'seriess':series, 
        'form':form,
        'search':search,
    }
    
    return render(request, 'putlist/series.html', context)




def add_zadan_form(request, pk):
    if request.method == 'POST':
        form = Zakazchiki(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.SPR_USER_FIN_ID = request.user
            instance.save()
            
            return HttpResponse('<script type="text/javascript">window.close(); window.opener.location.reload(false);</script>')
    else:
        form = Zakazchiki(pk)
    return render(request, 'putlist/forms/add_zadan_form.html', {'form': form})
