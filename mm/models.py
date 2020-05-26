from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, null=True, blank=True)
    country = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    # TODO split out titles and teams eventually
    title = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    segment = models.CharField(max_length=255)
    manager = models.ForeignKey("Person", on_delete=models.CASCADE,
                                null=True, blank=True, related_name='employee')

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def tenure(self):
        rd = relativedelta(datetime.now(), self.start_date)
        years = f'{rd.years} years, ' if rd.years > 0 else ''
        months = f'{rd.months} months, ' if rd.months > 0 else ''
        days = f'{rd.days} days' if rd.days > 0 else ''
        return f'{years}{months}{days}'


class Win(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now())
