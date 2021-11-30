from django.core.exceptions import ValidationError
from .base import BusinessLogicObject

def price_validator(price):
    print("I am validator in Product.py")
    if not price > 0:
        raise ValidationError(('The price cannot be less or equal then zero.'))

class Product_bl(BusinessLogicObject):
    def __init__(self, productID=None, productType=None, productName=None, description=None, stock=None, price=None, args = None):
        if not args:
            self.productID = productID
            self.productType = productType
            self.productName= productName
            self.description = description
            self.stock = stock
            self.price = price
            self.pk = self.getID()
        else:
            self.updateFromDict(args)

    def __repr__(self):
        return "<" + self.__class__.__name__ + f" {self.getID()}> " + " " + str(self.productName)

    def getID(self):
        return self.productID

    def updateFromDict(self, args):
        self.productName = args['productName']
        self.productType = args['productType']
        self.productID = args['productID']
        self.description = args['description']
        self.stock = args['stock']
        self.price = args['price']
        self.pk = self.getID()
        return


