from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.gis.admin import GeoModelAdmin


from .models import AME
from .models import Answer, AnswerGPS, AnswerGS, AnswerHHMembers, AnswerNR, Price


@admin.register(AME)
class AMEAdmin(ImportExportModelAdmin):
    pass


@admin.register(AnswerGPS)
class AnswerGPSAdmin(ImportExportModelAdmin):
    pass


class AnswerGPSInline(admin.StackedInline):
    model = AnswerGPS

# TODO get base map to show
# admin.site.register(AnswerGPS, GeoModelAdmin)


@admin.register(AnswerGS)
class AnswerGSAdmin(ImportExportModelAdmin):
    pass


class AnswerGSInline(admin.StackedInline):
    model = AnswerGS
    extra = 1


@admin.register(AnswerHHMembers)
class AnswerHHMembersAdmin(ImportExportModelAdmin):
    pass


class AnswerHHMembersInline(admin.StackedInline):
    model = AnswerHHMembers
    extra = 1


@admin.register(AnswerNR)
class AnswerNRAdmin(ImportExportModelAdmin):
    pass


class AnswerNRInline(admin.StackedInline):
    model = AnswerNR
    extra = 1


@admin.register(Answer)
class AnswerAdmin(ImportExportModelAdmin):
    """
    Admin class for Connections
    """
    #list_display = ['dataset_id']
    inlines = [AnswerGPSInline, AnswerGSInline, AnswerHHMembersInline, AnswerNRInline]


@admin.register(Price)
class PriceAdmin(ImportExportModelAdmin):
    """
    Admin class for Connections
    """
    list_display = ['dataset_uuid', 'village', 'gs', 'price']


