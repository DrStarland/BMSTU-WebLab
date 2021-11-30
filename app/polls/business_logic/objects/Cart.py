from django.urls import reverse
from .base import BusinessLogicObject

class Cart_bl(BusinessLogicObject):
    def __init__(self, cartID=None, memberID=None, productIDs=None,
        productQuantities=None, quantity=None, args=None):
        if not args:
            self.cartID = cartID
            self.memberID = memberID
            self.productIDs = productIDs
            self.productQuantities = productQuantities
            self.quantity = quantity
            self.pk = self.getID()
        else:
            self.updateFromDict(args)

    def __repr__(self):
        return f"<" + self.__class__.__name__ + f" #{self.getID()}> " + " " + str(self.memberID)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.cartID)])

    def getID(self):
        return self.cartID

    def updateFromDict(self, args):
        self.cartID = args['cartID']
        self.memberID = args['memberID']
        self.productIDs = args['productIDs']
        self.productQuantities = args['productQuantities']
        self.quantity = args['quantity']
        self.pk = self.getID()
        return