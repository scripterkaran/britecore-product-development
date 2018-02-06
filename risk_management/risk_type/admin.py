from django.contrib import admin
from .models import RiskType, RiskTypeField

class RiskTypeFieldInline(admin.TabularInline):
    model = RiskTypeField

class RiskTypeAdmin(admin.ModelAdmin):
    search_fields = ('name' ,)
    list_display = ('name','template', 'get_form_fields')
    inlines = (RiskTypeFieldInline,)

    def get_form_fields(self, obj):
        return ",".join([p.__str__() for p in obj.fields.all()])


class RiskFieldTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__','type', 'risk_type')


admin.site.register(RiskType,RiskTypeAdmin )
admin.site.register(RiskTypeField,RiskFieldTypeAdmin)
