from django.urls import path
from .views import ReportList

urlpatterns = [
  
    path('', ReportList.as_view(), name='reports-list'),
]
