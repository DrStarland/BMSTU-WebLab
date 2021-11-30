#from django.conf import settings
#from django.core.checks import messages
from django.db.models.deletion import CASCADE
from django.urls import reverse
#from django.contrib.postgres.fields import ArrayField
from django.db import models

import uuid
import os

from .ProductType import *
from ..business_logic.objects import Product as domain_model

def custom_save_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/', filename)

    # licnum = models.CharField(
    #     max_length=15, unique=True, validators=[validate_licnum])
  

class Product(models.Model):
    productID = models.IntegerField(primary_key=True)
    productType = models.ForeignKey(ProductType,  on_delete=CASCADE)
    productName = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.IntegerField()
    imageSource = models.ImageField(upload_to=custom_save_path,
                            verbose_name='изображение', default='img/image.png')


    def __str__(self):
        return self.__class__.__name__ + " " + str(self.productName) + ": " + str(self.description)

    def get_absolute_url(self):
        return reverse('industry-detail', args=[str(self.productID)])

    @staticmethod
    def update_from_domain(bl_object):
        try:
            b = Product.objects.get(productID=bl_object.productID)
            print("huh?")
        except Product.DoesNotExist:
            b = Product(productID=bl_object.productID)
        b.productName = bl_object.productName
        b.productType = bl_object.productType
        b.productID = bl_object.productID
        b.description = bl_object.description
        b.stock = bl_object.stock
        b.price = bl_object.price
        print("save was?")
        b.save()
        print("yes")

    def to_domain(self):
        b = domain_model.Product_bl(
            productName=self.productName,
            productType=self.productType,
            productID = self.productID,
            description = self.description,
            stock = self.stock,
            price = self.price
        )
        return b
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'