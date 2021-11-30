from django.urls import reverse
from django.db import models
import uuid
import os

from ..business_logic.objects import ProductType as domain_model

class ProductType(models.Model):
    typeID = models.SmallIntegerField(primary_key=True)
    typeName = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return str(self.typeName) + ": " + str(self.description)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.typeID)])

    @staticmethod
    def update_from_domain(bl_object):
        try:
            b = ProductType.objects.get(typeID=bl_object.typeID)
        except ProductType.DoesNotExist:
            b = ProductType(typeID=bl_object.typeID)
        b.typeID = bl_object.typeID
        b.typeName = bl_object.typeName
        b.description = bl_object.description
        b.save()
        # b.allocation_set.set(
        #     Allocation.from_domain(l, b)
        #     for l in product._allocations
        # )

    def to_domain(self):
        b = domain_model.ProductType_bl(
            typeID = self.typeID,
            typeName = self.typeName,
            description = self.description
        )
        # b._allocations = set(
        #     a.line.to_domain()
        #     for a in self.allocation_set.all()
        # )
        return b
    
    class Meta:
        verbose_name = 'тип'
        verbose_name_plural = 'типы'