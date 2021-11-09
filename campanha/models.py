from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.deletion import PROTECT
from django.utils.timezone import now


class Campanha(models.Model):

    class Status(models.TextChoices):
        ENABLED = "Enabled"
        DISABLED = "Disabled"

    name = models.CharField(max_length=50, blank=True, null=True)
    start = models.DateField(default=now)
    end = models.DateField()
    description = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(_('Status'), max_length = 8, choices = Status.choices, default = Status.ENABLED)
    donor = models.ForeignKey("accounts.User", on_delete=PROTECT,null=True, related_name="donor")
    donee = models.ForeignKey("accounts.User", on_delete=PROTECT,null=True, related_name="donee")

    def __str__(self):
        return self.name


class DonationItem(models.Model):

    item = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(default=now)
    volume = models.IntegerField()
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, null=True, related_name="campanha")
