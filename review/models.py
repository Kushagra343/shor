from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
	#user = models.ForeignKey(User)
    user = models.CharField(max_length=200, verbose_name = 'User name')
    address = models.CharField(max_length=200, verbose_name = 'Address in String format')
    verified_by = models.BooleanField( verbose_name = 'Verified by the person name')
    def __str__(self):
        return str(self.id)
    class Meta:
            db_table = 'Review'
            verbose_name = 'Review'
            verbose_name_plural = 'Reviews'

class Attributes(models.Model):
    review = models.ForeignKey(Review, verbose_name = 'ForeignKey relation to the model Review')
    key = models.CharField(max_length=200, verbose_name = 'Attribute Type')
    value = models.CharField(max_length=200, verbose_name = 'Attribute Value')
    def __str__(self):
        return str(self.id)
    class Meta:
            db_table = 'Attribute'
            verbose_name = 'Attribute'
            verbose_name_plural = 'Attributes'