from django.db import models
# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=200) 	  
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    def __str__(self):
        return str(self.user)
    class Meta:
    	    db_table = 'Address'
    	    verbose_name = 'Address'
    	    verbose_name_plural = 'Addresss'
	

class Address_detail(models.Model):
    address = models.ForeignKey(Address)
    property_type = models.CharField(max_length=20)
    attributes = models.CharField(max_length=500) 	 	  	
    def __str__(self):
        return str(self.user)
    class Meta:
    	    db_table = 'Address_detail'
    	    verbose_name = 'Address_detail'
    	    verbose_name_plural = 'Address_details'
