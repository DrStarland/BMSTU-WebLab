from django.urls import reverse
from .base import BusinessLogicObject

class Comment_bl(BusinessLogicObject):
    def __init__(self, commentID=None, memberID=None, productID=None, message=None, commentDate=None, args=None):
        if not args: 
            self.commentID = commentID
            self.memberID = memberID
            self.productID = productID
            self.message = message
            self.commentDate = commentDate
            self.pk = self.getID()
        else:
            self.updateFromDict(args)

    def __repr__(self):
        return "<" + self.__class__.__name__ + f" #{self.commentID}> " + " " + str(self.memberID) + " " + str(self.productID)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.commentID)])

    def getID(self):
        return self.commentID

    def updateFromDict(self, args):
        self.commentID = args['commentID']
        self.memberID = args['productID']
        self.message = args['message']
        self.commentDate = args['commentDate']
        self.pk = self.getID()
        return

    
