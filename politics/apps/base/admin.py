from django.contrib import admin
from apps.base.models.politician import Politician
from apps.base.models.education import PoliticianEducation


class EducationInline(admin.TabularInline):
    model = PoliticianEducation
    fields = [
        "category", "name", "specialization",
        "university", "grade", "start", "end"
    ]
    # readonly_fields = fields
    can_delete = True
    # show_change_link = True

class PoliticianAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    inlines = [EducationInline]

admin.site.register(Politician,PoliticianAdmin)
