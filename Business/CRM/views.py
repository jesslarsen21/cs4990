from django.shortcuts import render

from .models import Campaign, Company, Contact, Stage, Opportunity, Reminder, Report, CallLog, OpportunityStage
from django.views.generic import ListView, UpdateView, CreateView, TemplateView, DetailView, FormView, DeleteView
from django.views.generic.detail import View, SingleObjectMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from viewsets import ModelViewSet
from django.db.models import Count
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.db.models import Count, Q
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.models import modelform_factory

# Create your views here.

#needed
class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)

class DashboardView(TemplateView):
    model = OpportunityStage
    template_name = "CRM/test_dash.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        #Adding OpportunityStages to the templates' context
        context["reminders"] = Reminder.objects.all().order_by('-date')[:5]

        context["opportunities"] = Opportunity.objects.all().order_by('-create_date')[:5]
        context["opportunity_stages"] = OpportunityStage.objects.all().order_by('-timestamp')[:5]
        context["stage_by_opp"] = Stage.objects.order_by('-order').annotate(opp_count = Count('opportunity'))
        context['top_list'] = User.objects.annotate(num_op=Count('opportunity')).order_by('-num_op')[:3]

        context["opp_users"] = User.objects.filter(opportunitystage__stage__stage = 100).annotate(num_opp=Count('opportunitystage'))[:5]


        return context

class CallListView(ListView):
    model = CallLog

class CallDetailView(DetailView):
    model = CallLog

class CallEditView(UpdateView):
    model = CallLog
    fields = ['note']

    def get_success_url(self):
        return reverse('CRM:calldetail', args=(self.object.pk,))

class AddCall(CreateView):

    model = CallLog
    fields = ['note']

    def get_success_url(self):
        return reverse('CRM:opportunitydetail', args=(self.kwargs['pk'],))

    def form_valid(self, form):
        call = form.save(commit=False)
        call.user = User.objects.filter(id=self.request.user.id)[0]
        call.opportunity = Opportunity.objects.get(id = self.kwargs['pk'])
        call.save()
        return super(AddCall, self).form_valid(form)

class CallDelete(DeleteView):
    model = CallLog
    success_url = reverse_lazy('CRM:calllist')
    

class ContactListView(ListView):
    model = Contact

class ContactDetailView(DetailView):
    model = Contact

class ContactEditView(UpdateView):
    model = Contact
    fields = ['company', 'first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone', 'email']

    def get_success_url(self):
        return reverse('CRM:contactdetail', args=(self.object.pk,))

class AddContact(CreateView):

    model = Contact
    fields = ['company', 'first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone', 'email']
    success_url = reverse_lazy('CRM:contactlist')



class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('CRM:contactlist')
    
    
class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyEditView(UpdateView):
    model = Company
    fields = ['name', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']

    def get_success_url(self):
        return reverse('CRM:companydetail', args=(self.object.pk,))

class AddCompany(CreateView):

    model = Company
    fields = ['name', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']
    success_url = reverse_lazy('CRM:companylist')

class CompanyDelete(DeleteView):
    model = Company

    success_url = reverse_lazy('CRM:companylist')

class ReminderDelete(DeleteView):
    model = Reminder

    success_url = reverse_lazy('CRM:reminderlist')
    
class ReminderListView(ListView):
    model = Reminder


class ReminderEditView(UpdateView):
    model = Reminder
    fields = ['opportunity', 'date', 'note', 'completed']

    success_url = reverse_lazy('CRM:reminderlist')



class AddReminder(ModelFormWidgetMixin, CreateView):
    model = Reminder
    fields = ['opportunity', 'date', 'note', 'completed']
    widgets = {
        'date': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}),
    }
    success_url = reverse_lazy('CRM:reminderlist')



class OpportunityListView(ListView):
    model = Opportunity


class OpportunityDetailView(DetailView):
    model = Opportunity
    #template_name = "CRM/test_opportunity_detail.html"




class OpportunityEditView(UpdateView):
    model = Opportunity
    fields = ['name', 'company', 'Contact', 'value', 'stage', 'source']

    def get_success_url(self):
        return reverse('CRM:opportunitydetail', args=(self.object.pk,))

    def form_valid(self, form):

        opportunity = form.save(commit=False)

        if opportunity.stage.stage != self.get_object().stage.stage:
            opportunity_stage = OpportunityStage()
            opportunity_stage.opportunity = opportunity
            opportunity_stage.stage = form.cleaned_data['stage']
            opportunity_stage.user = self.request.user
            opportunity_stage.save()

        opportunity.save()

        return super(OpportunityEditView, self).form_valid(form)


class AddOpportunity(CreateView):

    model = Opportunity
    fields = ['name', 'company', 'Contact', 'value', 'source', 'stage', 'user']
    success_url = reverse_lazy('CRM:opportunitylist')

    def form_valid(self, form):
        opportunity = form.save(commit=False)
        opportunity.user = User.objects.filter(id=self.request.user.id)[0]
        opportunity.save()
        if opportunity.stage.value != self.get_object().stage.value:
            opportunity_stage = OpportunityStage()
            opportunity_stage.opportunity = opportunity
            opportunity_stage.stage = form.cleaned_data['stage']
            opportunity_stage.user = self.request.user
            opportunity_stage.save()

        opportunity.save()

        return super(AddOpportunity, self).form_valid(form)

class OpportunityDelete(DeleteView):
    model = Opportunity

    success_url = reverse_lazy('CRM:opportunitylist')


class OpportunityStageAdd(CreateView):

    model = OpportunityStage
    fields = ['opportunity', 'stage', 'user']
    def get_success_url(self):
        return reverse('CRM:opportunitydetail', args=(self.object.pk,))

class SearchResultsView(TemplateView):
    template_name = 'CRM/search_results.html'
    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)

        # If we don't have a search term in the URL, just return the context as is.
        # Otherwise, populate the template context with potential search results.
        if not self.request.GET.get("q", None):
            return context

        term = self.request.GET["q"] # save off the search term for convenience
        context['searchterm'] = term # send the search term to the template's context
        context['contact_list'] = Contact.objects.all().filter(
            Q(first_name__icontains = term) | Q(last_name__icontains = term))
        context['company_list'] = Company.objects.all().filter(name__icontains = term)
        context['reminder_list'] = Reminder.objects.all().filter(note__icontains = term)
        context['calllog_list'] = CallLog.objects.all().filter(note__icontains = term)
        context['opportunity_list'] = Opportunity.objects.all().filter(
            Q(Contact__first_name__icontains = term) | Q(Contact__last_name__icontains = term) | Q(stage__name__icontains = term))

        return context