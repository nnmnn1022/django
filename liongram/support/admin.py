from django.contrib import admin

from support.models import Faq

# Register your models here.
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin): 
    list_display = ('question','category','answer','created_by','created_at','last_modifier','modified_at')