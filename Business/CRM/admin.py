from django.contrib import admin
from .models import Campaign, Company, Contact, Stage, Opportunity, Reminder, Report, CallLog, OpportunityStage
# Register your models here.
admin.site.register(Campaign)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Stage)
admin.site.register(Opportunity)
admin.site.register(Reminder)
admin.site.register(Report)
admin.site.register(CallLog)
admin.site.register(OpportunityStage)