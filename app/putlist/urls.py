from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('second/', views.second, name="second"),
    #tables
    path('', login_required(views.index), name="index"),
    path('spravochniki/', login_required(views.spravochniki), name="spravochniki"),
    path('car/', login_required(views.car), name="car"),
    path('driver/', login_required(views.driver), name="driver"),
    path('toplivo/', login_required(views.toplivo), name="toplivo"),
    path('organizations/', login_required(views.organizations), name="organizations"),
    path('timeWork/', login_required(views.timeWork), name="timeWork"),
    path('series/', login_required(views.series), name="series"),
    #forms
    path('Form_index/', login_required(views.Form_index), name="Form_index"),
    path('Form_index_TWObtn/', login_required(views.Form_index_TWObtn), name="Form_index_TWObtn"),
    
    path('add_zadan/<int:pk>/', login_required(views.add_zadan_form), name="add_zadan"),
    #delete
    path('ajax/delete2/', login_required(views.NewDelete2.as_view()), name="delete2"),#машины
    path('ajax/delete3/', login_required(views.NewDelete3.as_view()), name="delete3"),#водители
    path('ajax/delete4/', login_required(views.Delete4.as_view()), name="delete4"),#заказчики
    path('ajax/delete5/', login_required(views.NewDelete5.as_view()), name="delete5"),#топливо
    path('ajax/delete6/', login_required(views.NewDelete6.as_view()), name="delete6"),#организ
    path('ajax/delete7/', login_required(views.NewDelete7.as_view()), name="delete7"),#режим
    path('ajax/delete8/', login_required(views.NewDelete8.as_view()), name="delete8"),#серияы

    path('ajax/delete/', login_required(views.Delete.as_view()), name="ajax_delete"),

    #update
    path('update/<int:pk>/', views.NewUpdate, name="update"),
    
    #url(r'^update/(?P<pk>\w+)/$', views.NewUpdate, name="update"),  
    path('<int:pk>/update2/', login_required(views.NewUpdate2.as_view()), name="update2"),
    
    path('render_pdf_view/<int:pk>/', login_required(views.render_pdf_view), name="render_pdf_view"),
  
  
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
