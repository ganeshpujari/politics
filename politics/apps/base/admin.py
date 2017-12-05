from django.contrib import admin
from apps.base.models.politician import Politician
from apps.base.models.education import PoliticianEducation
from apps.base.models.work import Work
from apps.base.models.family_description import PoliticianFamily
from apps.base.models.achievements import Achievements
from apps.base.models.assets import PoliticianAssets
from apps.base.models.media import Media

class EducationInline(admin.TabularInline):
    model = PoliticianEducation
    fields = [
        "category", "name", "specialization",
        "university", "start", "end"
    ]
    extra = 1
    can_delete = True

class AchievementsInline(admin.TabularInline):
    model = Achievements
    fields = [
        "title", "start", "end",
    ]
    extra = 1
    can_delete = True

class MediaInline(admin.TabularInline):
    model = Media
    fields = [
        "type", "title", "url",

    ]
    extra = 1
    can_delete = True

class EducationInline(admin.TabularInline):
    model = PoliticianEducation
    fields = [
        "category", "name", "specialization",
        "university", "start", "end"
    ]
    extra = 1
    can_delete = True

class PoliticalWorkInline(admin.TabularInline):
    model = Work
    fields = [
        "type","title", "description", "start",
        "end",'city','state','country','latitude','longitude'
    ]

    extra = 1
    can_delete = True




class PoliticianFamilyInline(admin.TabularInline):
    model = PoliticianFamily
    fields = [
        "relation","name", "date_of_birth", "occupation",

    ]

    extra = 1
    can_delete = True

class PoliticianAssetsInline(admin.TabularInline):
    model = PoliticianAssets
    fields = [
        "type","name","current_price",

    ]

    extra = 1
    can_delete = True

class PoliticianAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    inlines = [EducationInline,PoliticalWorkInline,PoliticianFamilyInline,PoliticianAssetsInline,MediaInline,AchievementsInline]

admin.site.register(Politician,PoliticianAdmin)
admin.site.register(Work)