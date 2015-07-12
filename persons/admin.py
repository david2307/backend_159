from django.contrib import admin

from .models import Person, Sex, Town, Departament, DocumentType
# Register your models here.
admin.site.register(Person)
admin.site.register(Sex)
admin.site.register(Town)
admin.site.register(Departament)
admin.site.register(DocumentType)