from django.db import models
from django.urls import reverse


class Sale(models.Model):
    invoice_id = models.CharField(max_length=20, blank=True)
    branch = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=20, blank=True)
    customer_type = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    product_line = models.CharField(max_length=50, blank=True)
    unit_price = models.FloatField(blank=True)
    quantity = models.IntegerField(blank=True)
    tax = models.FloatField(blank=True)
    total = models.FloatField(blank=True)
    date = models.DateField(auto_now=False, blank=True)
    payment_method = models.CharField(max_length=50, blank=True)
    cogs = models.FloatField(blank=True)
    gross_income = models.FloatField(blank=True)
    rating = models.FloatField(blank=True)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return self.invoice_id

    def get_absolute_url(self):
        return reverse('view_sale', args=[self.invoice_id])
