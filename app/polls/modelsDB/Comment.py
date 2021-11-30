from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models

from .Member import *
from .Product import *

from ..business_logic.objects import Comment as domain_model

class Comment(models.Model):
    commentID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=CASCADE)
    productID = models.ForeignKey(Product, on_delete=CASCADE)
    message = models.TextField()
    commentDate = models.DateField()

    def __str__(self):
        return str(self.message) + str(self.commentDate)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.commentID)])
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    @staticmethod
    def update_from_domain(bl_object):
        try:
            b = Comment.objects.get(commentID=bl_object.commentID)
        except Comment.DoesNotExist:
            b = Comment(commentID=bl_object.commentID)
        b.commentID = bl_object.commentID
        b.memberID = bl_object.memberID
        b.productID = bl_object.productID
        b.message = bl_object.message
        b.commentDate = bl_object.commentDate
        b.save()
        # b.allocation_set.set(
        #     Allocation.from_domain(l, b)
        #     for l in product._allocations
        # )

    def to_domain(self):
        b = domain_model.Comment_bl(
            commentID = self.commentID,
            memberID = self.memberID,
            productID = self.productID,
            message = self.message,
            commentDate = self.commentDate
        )
        # b._allocations = set(
        #     a.line.to_domain()
        #     for a in self.allocation_set.all()
        # )
        return b