"""Business URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from viewsets import ModelViewSet
from . import views
from views import *

urlpatterns = [
    url(r'^$', login_required(views.DashboardView.as_view()), name="dashboard"),
    url(r'^search/$', login_required(views.SearchResultsView.as_view()), name="search"),
    url(r'^calls/$', login_required(views.CallListView.as_view()), name="calllist"),
    url(r'^calls/(?P<pk>\d+)/$', login_required(views.CallDetailView.as_view()), name="calldetail"),
    url(r'^calls/(?P<pk>\d+)/edit/$', login_required(views.CallEditView.as_view()), name="editcall"),
    url(r'^calls/add/$', login_required(views.AddCall.as_view()), name = "addcall"),
    url(r'^calls/(?P<pk>\d+)/delete/$', login_required(views.CallDelete.as_view()), name="calldelete"),

    #url(r'^searchresults/$', login_required(views.CallDelete.as_view()), name="search"),

    url(r'^opportunity/(?P<pk>\d+)/$', login_required(views.OpportunityDetailView.as_view()), name="opportunitydetail"),
    url(r'^opportunity/$', login_required(views.OpportunityListView.as_view()), name="opportunitylist"),
    url(r'^opportunity/(?P<pk>\d+)/edit/$', login_required(views.OpportunityEditView.as_view()), name="opportunityedit"),
    url(r'^opportunity/add/$', login_required(views.AddOpportunity.as_view()), name = "opportunityadd"),
    url(r'^opportunity/(?P<pk>\d+)/delete/$', login_required(views.OpportunityDelete.as_view()), name="opportunitydelete"),

    url(r'^contact/(?P<pk>\d+)/$', login_required(views.ContactDetailView.as_view()), name="contactdetail"),
    url(r'^contact/$', login_required(views.ContactListView.as_view()), name="contactlist"),
    url(r'^contact/(?P<pk>\d+)/edit/$', login_required(views.ContactEditView.as_view()), name="contactedit"),
    url(r'^contact/add/$', login_required(views.AddContact.as_view()), name = "contactadd"),
    url(r'^contact/(?P<pk>\d+)/delete/$', login_required(views.ContactDelete.as_view()), name="contactdelete"),
    
    url(r'^company/(?P<pk>\d+)/$', login_required(views.CompanyDetailView.as_view()), name="companydetail"),
    url(r'^company/$', login_required(views.CompanyListView.as_view()), name="companylist"),
    url(r'^company/(?P<pk>\d+)/edit/$', login_required(views.CompanyEditView.as_view()), name="companyedit"),
    url(r'^company/add/$', login_required(views.AddCompany.as_view()), name = "companyadd"),
    url(r'^company/(?P<pk>\d+)/delete/$', login_required(views.CompanyDelete.as_view()), name="companydelete"),

    url(r'^reminders/$', login_required(views.ReminderListView.as_view()), name="reminderlist"),
    url(r'^reminders/(?P<pk>\d+)/edit/$', login_required(views.ReminderEditView.as_view()), name="reminderedit"),
    url(r'^reminders/add/$', login_required(views.AddReminder.as_view()), name = "reminderadd"),
    url(r'^reminders/(?P<pk>\d+)/delete/$', login_required(views.ReminderDelete.as_view()), name="reminderdelete"),

    url(r'^reports/$', login_required(views.CallDelete.as_view()), name="reports"),
    
    url(r'^stages/(?P<pk>\d+)/$', login_required(views.CallListView.as_view()), name="stagesdetail"),
    url(r'^stages/$', login_required(views.CallListView.as_view()), name="stageslist"),

    url(r'^opportunitystages/add/$', login_required(views.OpportunityStageAdd.as_view()), name="opportunitystageadd"),
]