from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models
from .Member import *
from .Product import *

from ..business_logic.objects import Rating as domain_model

class Rating(models.Model):
    ratingID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=CASCADE)
    productID = models.ForeignKey(Product, on_delete=CASCADE)
    value = models.SmallIntegerField()

    def __str__(self):
        return "ID: " + str(self.productID) + ", rating: " + str(self.value)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.ratingID)])
    
    class Meta:
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'

    @staticmethod
    def update_from_domain(bl_object):
        try:
            b = Rating.objects.get(ratingID=bl_object.ratingID)
        except Rating.DoesNotExist:
            b = Rating(ratingID=bl_object.ratingID)
        b.ratingID = bl_object.ratingID
        b.memberID = bl_object.memberID
        b.productID = bl_object.productID
        b.value = bl_object.value
        b.save()
        # b.allocation_set.set(
        #     Allocation.from_domain(l, b)
        #     for l in product._allocations
        # )

    def to_domain(self):
        b = domain_model.Rating_bl(
            ratingID = self.ratingID,
            memberID = self.memberID,
            productID = self.productID,
            value = self.value
        )
        # b._allocations = set(
        #     a.line.to_domain()
        #     for a in self.allocation_set.all()
        # )
        return b