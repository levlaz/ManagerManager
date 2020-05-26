from django.urls import path, include
from django.views.generic import TemplateView
from mm.views import PersonDetailView, ReportingStructureView, DashboardView

app_name = 'mm'
urlpatterns = [
    path('', TemplateView.as_view(template_name="mm/base.html")),
    path('auth/', include('django.contrib.auth.urls')),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('reporting/', ReportingStructureView.as_view(), name='reporting'),
    path('person/<int:pk>/', PersonDetailView.as_view(),
         name='person-detail')
]
