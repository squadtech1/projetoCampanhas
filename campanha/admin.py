from django.contrib import admin
from .models import Campanha, DonationItem


class DonationItemInline(admin.TabularInline):
    model = DonationItem

class CampanhaAdmin(admin.ModelAdmin):
    inlines = [DonationItemInline,]

admin.site.register(Campanha, CampanhaAdmin)
admin.site.register(DonationItem)
