from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'mm'
urlpatterns = [
    path('', TemplateView.as_view(template_name="mm/base.html")),
    path('auth/', include('django.contrib.auth.urls'))
]
