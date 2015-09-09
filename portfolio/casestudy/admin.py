from django.contrib import admin
# Register your models here.
from .models import CaseStudy, Item

class CaseStudyAdmin(admin.ModelAdmin):
   pass

admin.site.register(CaseStudy, CaseStudyAdmin)
admin.site.register(Item)

