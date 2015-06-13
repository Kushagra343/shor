from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Flat(models.Model):
a    user = models.ForeignKey(User)
    flat_type = models.CharField(max_length=6)	  
    locality = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)	
    pincode = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()	
    name =  models.CharField(max_length=50)
    block =  models.CharField(max_length=20)
    floor = models.IntegerField() 	  
    room_num = models.CharField(max_length=20)   		
    def __str__(self):
        return str(self.name)
    class Meta:
    	    db_table = 'Flat'
    	    verbose_name = 'Flat'
    	    verbose_name_plural = 'Flats'


class Hostel(models.Model):
    user = models.ForeignKey(User)
    flat_type = models.CharField(max_length=6)
    locality = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)	
    pincode = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    name =  models.CharField(max_length=50)		  
    floor = models.IntegerField() 	  
    room_num = models.CharField(max_length=20)
    def __str__(self):
        return str(self.name)
    class Meta:
    	    db_table = 'Hostel'
    	    verbose_name = 'Hostel'
    	    verbose_name_plural = 'Hostels'


class House(models.Model):
    user = models.ForeignKey(User)
    flat_type = models.CharField(max_length=6)
    locality = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)	
    pincode = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    name =  models.CharField(max_length=50)		
    house_num = models.CharField(max_length=20) 	  
    def __str__(self):
        return str(self.name)
    class Meta:
    	    db_table = 'House'
    	    verbose_name = 'House'
    	    verbose_name_plural = 'Houses'

