from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', login_required(views.ClockInOutView.as_view()), name="ko"),
   url(r'^report/$', login_required(views.ReportView.as_view()), name="report"),
   url(r'^mypunches/$', login_required(views.MyPunches.as_view()), name = "mypunches")
]
