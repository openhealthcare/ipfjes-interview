from django.contrib import admin
from ipfjes import models

class SocCodeAdmin(admin.ModelAdmin):
    search_fields = ['title', 'soc90', 'soc2000']
    list_display = ['title', 'soc90', 'soc2000']


admin.site.register(models.SocCode, SocCodeAdmin)
