from django.db import models

# Create your models here.

class ComplaintMessage(models.Model):
    name = models.CharField(max_length=200, blank=True, null=False)
    email = models.CharField(max_length=200, blank=True, null=False)
    phone = models.CharField(max_length=200, blank=True, null=False)
    country = models.CharField(max_length=200, blank=True, null=False)
    amount = models.CharField(max_length=200, blank=True, null=False)
    transaction = models.CharField(max_length=200, blank=True, null=False)
    comment = models.TextField(blank=True, null=False)
    tmethod = models.CharField(verbose_name="Transfer method", max_length=200, blank=True, null=False)

    def __str__(self):
        return self.name + " - " + self.email + " sent a complaint. "
    
    class Meta:
        verbose_name_plural = "User Complaints"
        verbose_name = "User Complaint"