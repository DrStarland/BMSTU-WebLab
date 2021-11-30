from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models

from .Member import * 

#from .ProductType import *
from ..business_logic.objects import Transaction as domain_model

class Transaction(models.Model):
    transactionID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=CASCADE)
    productIDs = ArrayField(models.IntegerField(), default=list())
    productQuantities = ArrayField(models.SmallIntegerField(), default=list())
    approvalStatus = models.CharField(max_length=10)
    transactionDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return "TID: " + str(self.transactionID) + ", status: " + str(self.approvalStatus)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.transactionID)])
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    @staticmethod
    def update_from_domain(bl_object):
        try:
            b = Transaction.objects.get(transactionID=bl_object.transactionID)
        except Transaction.DoesNotExist:
            b = Transaction(transactionID=bl_object.transactionID)
        b.transactionID = bl_object.transactionID 
        b.memberID = bl_object.memberID
        b.productIDs = bl_object.productIDs
        b.productQuantities = bl_object.productQuantities
        b.approvalStatus = bl_object.approvalStatus
        b.transactionDate = bl_object.transactionDate
        b.save()
        # b.allocation_set.set(
        #     Allocation.from_domain(l, b)
        #     for l in product._allocations
        # )

    def to_domain(self):
        b = domain_model.Transaction_bl(
            transactionID =self.transactionID ,
            memberID=self.memberID,
            productIDs = self.productIDs,
            productQuantities = self.productQuantities,
            approvalStatus = self.approvalStatus,
            transactionDate = self.transactionDate
        )
        # b._allocations = set(
        #     a.line.to_domain()
        #     for a in self.allocation_set.all()
        # )
        return b