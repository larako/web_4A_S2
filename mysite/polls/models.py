from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User as Users

#class User(models.Model):
#	first_name = models.CharField(max_length=30)
#	last_name = models.CharField(max_length=30)
#	email = models.CharField(max_length=40)
#	password = models.CharField(max_length=30)
#	pseudo = models.CharField(max_length=30)
#	role = models.CharField(max_length=30)
#
#	def __str__(self):
#		return self.last_name

class Categories(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name

class Artistes(models.Model):
	name = models.CharField(max_length=30)
	pictures=models.ImageField(upload_to='artistes/', null='True', blank='True')
	def __str__(self):
		return self.name

class Spectacles(models.Model):
	name = models.CharField(max_length=255)
	place =models.CharField(max_length=100)
	beginningdate = models.DateField(null='True', blank='True')
	endingdate = models.DateField(null='True', blank='True')	
	price = models.IntegerField()
	description = models.CharField(max_length=255, default="")
	pictures=models.CharField(max_length=100,default="")
	artistes= models.ManyToManyField(Artistes,blank='true')
	categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Resource(models.Model):
	name=models.CharField( max_length=250 )
	location = models.CharField( max_length=250 )
	price = models.DecimalField( decimal_places=2, max_digits=7 )

class Purchase( models.Model ):
	Spectacles = models.IntegerField()
	purchaser = purchaser = models.IntegerField( )
	purchased_at = models.DateTimeField(auto_now_add=True)
	tx = models.IntegerField()




 





# Create your models here.
