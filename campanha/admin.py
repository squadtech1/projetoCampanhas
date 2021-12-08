from django.contrib import admin
from .models import Campanha, DonationItem, Post, DoneeNeed


class DonationItemInline(admin.TabularInline):
    model = DonationItem

class CampanhaAdmin(admin.ModelAdmin):
    inlines = [DonationItemInline,]

admin.site.register(Campanha, CampanhaAdmin)
admin.site.register(DonationItem)
admin.site.register(Post)
admin.site.register(DoneeNeed)
