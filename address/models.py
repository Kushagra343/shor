from django.db import models
# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=200, verbose_name = 'Address in String format')
    long_position = models.DecimalField(max_digits=9, decimal_places=6, verbose_name = 'Longitudnal position of the place')
    lat_position = models.DecimalField(max_digits=9, decimal_places=6, verbose_name = 'Latitudnal position of the place')
    def __str__(self):
        return str(self.id)
    class Meta:
            db_table = 'Address'
            verbose_name = 'Address'
            verbose_name_plural = 'Addresss'


class Attributes(models.Model):
    address = models.ForeignKey(Address, verbose_name = 'ForeignKey relation to the model Address')
    key = models.CharField(max_length=200, verbose_name = 'Attribute Type')
    value = models.CharField(max_length=200, verbose_name = 'Attribute Value')
    def __str__(self):
        return str(self.id)
    class Meta:
            db_table = 'Address_detail'
            verbose_name = 'Address_detail'
            verbose_name_plural = 'Address_details'
