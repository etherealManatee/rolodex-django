from django.contrib import admin
from contactbook.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "number")

# Register your models here.
admin.site.register(Contact, ContactAdmin)
