from django.contrib import admin
from gtfs.models import *

class StopInline(admin.StackedInline):
    model = Stop
    extra = 0
    
class RouteInline(admin.StackedInline):
    model = Route
    extra = 0
    
class AgencyInline(admin.StackedInline):
    model = Agency
    extra = 1

class DataSetAdmin(admin.ModelAdmin):
    inlines = [AgencyInline,]
    list_display = ['name', 'note', ]
    
class TimezoneAdmin(admin.ModelAdmin):
    pass

class LanguageAdmin(admin.ModelAdmin):
    pass

class AgencyAdmin(admin.ModelAdmin):
    inlines = [RouteInline, ]

class StopAdmin(admin.ModelAdmin):
    list_display = ['name','lat','lon']

class RouteAdmin(admin.ModelAdmin):
    list_filter = ['agency',]
    list_display = ['route_short_name','route_long_name', 'route_desc']


admin.site.register(DataSet, DataSetAdmin)

admin.site.register(Timezone, TimezoneAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Agency, AgencyAdmin)

admin.site.register(Stop, StopAdmin)
admin.site.register(Route, RouteAdmin)