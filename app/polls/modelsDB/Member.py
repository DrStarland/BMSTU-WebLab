from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models

from ..business_logic.objects import Member as domain_model

class Member(models.Model):
    memberID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('industry-detail', args=[str(self.memberID)])

    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'

    @staticmethod
    def update_from_domain(bl_object):
        try:
            b = Member.objects.get(memberID=bl_object.memberID)
        except Member.DoesNotExist:
            b = Member(memberID=bl_object.memberID)
        b.memberID = bl_object.memberID
        b.username = bl_object.username
        b.password = bl_object.password
        b.email = bl_object.email
        b.fullname = bl_object.fullname
        b.address = bl_object.address
        b.phone = bl_object.phone
        b.save()
        # b.allocation_set.set(
        #     Allocation.from_domain(l, b)
        #     for l in product._allocations
        # )

    def to_domain(self):
        b = domain_model.Member_bl(
            memberID=self.memberID,
            username=self.username,
            password = self.password,
            email = self.email,
            fullname = self.fullname,
            address = self.address,
            phone = self.phone
        )
        # b._allocations = set(
        #     a.line.to_domain()
        #     for a in self.allocation_set.all()
        # )
        return b