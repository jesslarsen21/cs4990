from django.shortcuts import render
from django.views import generic

from .models import CaseStudy, Item

# Create your views here.

## your views are your different pages on the website


class IndexView(generic.ListView):
   template_name = "casestudy/index.html"
   model = CaseStudy
   
class DetailView(generic.DetailView):
   template_name = "casestudy/details.html"
   model = CaseStudy
   
