from django.urls import reverse
from .base import BusinessLogicObject

class Rating_bl(BusinessLogicObject):
    def __init__(self, ratingID=None, memberID=None, productID=None, value=None, args=None):
        if not args:
            self.ratingID = ratingID
            self.memberID = memberID
            self.productID = productID
            self.value = value

            self.pk = self.getID()
        else:
            self.updateFromDict(args)

    def __repr__(self):
        return f"<" + self.__class__.__name__ + f" {self.getID()}> " + " " + str(self.memberID)

    def getID(self):
        return self.ratingID

    def updateFromDict(self, args):
        self.ratingID = args['ratingID']
        self.memberID = args['memberID']
        self.productID = args['productID']
        self.value = args['value']

        self.pk = self.getID()
        return
