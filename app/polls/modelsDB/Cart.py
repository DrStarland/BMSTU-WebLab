from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models
from .Member import *
from ..business_logic.objects import Cart as domain_model

class Cart(models.Model):
    cartID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=CASCADE)
    productIDs = ArrayField(models.IntegerField())
    productQuantities = ArrayField(models.SmallIntegerField())
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.cartID)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.cartID)])
    
    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
    
    @staticmethod
    def update_from_domain(bl_object):
        try:
            b = Cart.objects.get(cartID=bl_object.cartID)
        except Cart.DoesNotExist:
            b = Cart(cartID=bl_object.cartID)
        b.cartID = bl_object.cartID
        b.memberID = bl_object.memberID
        b.productIDs = bl_object.productIDs
        b.productQuantities = bl_object.productQuantities
        b.quantity = bl_object.quantity
        b.save()
        # b.allocation_set.set(
        #     Allocation.from_domain(l, b)
        #     for l in product._allocations
        # )

    def to_domain(self):
        b = domain_model.Cart_bl(
            cartID = self.cartID,
            memberID = self.memberID,
            productIDs = self.productIDs,
            productQuantities = self.productQuantities,
            quantity = self.quantity
        )
        # b._allocations = set(
        #     a.line.to_domain()
        #     for a in self.allocation_set.all()
        # )
        return b