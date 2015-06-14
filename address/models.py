from django.db import models
# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=200)
    long_position = models.DecimalField(max_digits=9, decimal_places=6)
    lat_position = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return str(self.id)
    class Meta:
            db_table = 'Address'
            verbose_name = 'Address'
            verbose_name_plural = 'Addresss'


class Attributes(models.Model):
    address = models.ForeignKey(Address)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)
    class Meta:
            db_table = 'Address_detail'
            verbose_name = 'Address_detail'
            verbose_name_plural = 'Address_details'
