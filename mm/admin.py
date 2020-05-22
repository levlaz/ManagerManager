from django.contrib import admin

from mm.models import Person, Win


class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'tenure')


admin.site.register(Person, PersonAdmin)
admin.site.register(Win)
