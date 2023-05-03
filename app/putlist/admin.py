from django.contrib import admin
from .models import  URL_TABLE, SPR_AUTO ,SPR_DRIVER, SPR_MARK_TOPL, SPR_ORG, SPR_REZHIM, SPR_SER, ZAKAZ
# Register your models here.
admin.site.register(URL_TABLE)
admin.site.register(SPR_DRIVER)
admin.site.register(SPR_MARK_TOPL)
admin.site.register(SPR_AUTO)
admin.site.register(SPR_ORG)
admin.site.register(SPR_REZHIM)
admin.site.register(SPR_SER)
admin.site.register(ZAKAZ)

