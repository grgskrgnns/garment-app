# api/models.py

#from django.db import models
from djongo import models
#from django.contrib.postgres.fields import ArrayField
#from django.contrib.auth import get_user_model

class Garment(models.Model):
    _id =  models.CharField(max_length=300)
    product_categories_mapped = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    source= models.CharField(max_length=100)
    url= models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    product_description= models.CharField(max_length=300)
    image_urls= models.TextField()
    #image_urls = ArrayField(models.CharField(max_length=300, blank=True),size=8)
    product_imgs_src= models.TextField()
    source= models.CharField(max_length=300)
    product_categories= models.TextField()
    images= models.TextField()
    path= models.CharField(max_length=300)
    checksum= models.CharField(max_length=100)
    position= models.TextField()
    product_title= models.CharField(max_length=300)
    brand= models.CharField(max_length=100)
    currency_code= models.CharField(max_length=100)
    stock= models.CharField(max_length=100)

    class Meta:
        app_label = "garments"
        db_table = "ITEMS"
   

    def __str__(self):
        return "%s - %s - %s - %s -%s - %s -%s -" % (self.product_id, self.gender, self.price, self.product_description, self.product_title, self.brand, self.stock)

