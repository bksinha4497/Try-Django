from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title=models.CharField(max_length=50)
	description=models.TextField(blank=True,null=True)
	price=models.DecimalField(decimal_places=2,max_digits=10000)
	summary=models.TextField()
	feature =models.BooleanField(default=False)#default=True ,null=True

	def get_absolute_url(self):
		return reverse("products:product-detail",kwargs={"id":self.id})
		#return f"/product/{self.id}"