from django.contrib import admin
from .models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'date_created',
       
        )


admin.site.register(Contacts,ContactsAdmin),
