from uuid import uuid4

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Client(models.Model):
    OPUWO = "OP"
    WINDHOEK = "WHK"
    WARMQUELLE = "WQ"
    TOWN = [
        ("OPUWO", "Opuwo"),
        ("WINDHOEK", "Windhoek"),
        ("WARMQUELLE", "Warmquelle"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    town = models.CharField("town", max_length=50, choices=TOWN)
    number_of_livestock = models.IntegerField(null=False, blank=False)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    date_join = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["-date_join"]

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if self.date_join is None:
            self.date_join = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify("{} {}".format(self.date_join, self.uniqueId))

        self.slug = slugify("{} {}".format(self.date_join, self.uniqueId))
        self.date_updated = timezone.localtime(timezone.now())
        super(Client, self).save(*args, **kwargs)


class Billing(models.Model):
    PENDING = "PE"
    OVERDUE = "OV"
    PAID = "PD"
    INVOICE_STATUS = [
        ("PENDING", "Pending"),
        ("OVERDUE", "Overdue"),
        ("PAID", "Paid"),
    ]
    title = models.CharField(null=True, blank=True, max_length=100)
    invoice_status = models.CharField(
        "status", max_length=50, choices=INVOICE_STATUS, default="PENDING"
    )
    note = models.CharField(null=True, blank=True, max_length=100)
    price_per_livestock = models.FloatField()
    discount_price = models.FloatField()

    # related fields
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="invoices",
        related_query_name="person",
    )

    # utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    date_created = models.CharField(max_length=100, null=True, blank=True)
    date_updated = models.CharField(max_length=100, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify("{} {}".format(self.date_created, self.uniqueId))

        self.slug = slugify("{} {}".format(self.date_created, self.uniqueId))
        self.date_updated = timezone.localtime(timezone.now())
        super(Billing, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("billing_detail", args=[str(self.slug)])
    

    # CALCULATING FARMER BILLING
    def price_of_livestocks(self):
        total = self.client.number_of_livestock * self.price_per_livestock
        return total

    def discount(self):
        if self.client.number_of_livestock <= 5:
            return self.discount_price * 0
        else:
            return self.discount_price

    def sub_total(self):
        s_total = self.client.number_of_livestock * self.price_per_livestock

        if self.client.number_of_livestock > 5:
            s_total = (
                self.client.number_of_livestock * self.price_per_livestock
            ) - self.discount_price
            return s_total

        return s_total

