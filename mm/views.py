from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from mm.models import Person


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        people = Person.objects.all()
        context = {'people': people}
        return render(request, 'mm/dashboard.html', context)


class ReportingStructureView(LoginRequiredMixin, View):
    def get(self, request):
        people = Person.objects.all()
        managers = [person for person in people if len(person.employee.all())
                                                       > 0]
        context = {'managers': managers}
        return render(request, 'mm/reports/reporting.html', context)


class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person
