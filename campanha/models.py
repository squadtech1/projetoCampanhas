from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.deletion import CASCADE, PROTECT
from django.utils.timezone import now


class Campanha(models.Model):
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique name')
        ]

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
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, null=True, related_name="donationItem")

    def __str__(self):
        return "Item: " + str(self.item) + " Volume: " + str(self.volume) + " Campanha: " + str(self.campanha.id)

class Post(models.Model):
    post = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey("accounts.User", on_delete=CASCADE,null=True, related_name="user")

class DoneeNeed(models.Model):
    need = models.CharField(max_length=50, blank=True, null=True)
    donee = models.ForeignKey("accounts.User", on_delete=CASCADE,null=True, related_name="user_donee_need")
