from django.core.exceptions import ValidationError
from .base import BusinessLogicObject

class Transaction_bl(BusinessLogicObject):
    def __init__(self, transactionID=None, memberID=None, productIDs=None, productQuantities=None,
        approvalStatus=None, transactionDate=None, args=None) :
        if not args:
            self.transactionID = transactionID
            self.memberID = memberID
            self.productIDs = productIDs
            self.productQuantities = productQuantities
            self.approvalStatus = approvalStatus
            self.transactionDate = transactionDate

            self.pk = self.getID()
        else:
            self.updateFromDict(args)

    def __repr__(self):
        return "<" + self.__class__.__name__ + f" {self.getID()}> " + " " + str(self.productIDs) + ": " + str(self.productQuantities)

    def getID(self):
        return self.transactionID

    def updateFromDict(self, args):
        self.transactionID = args['transactionID']
        self.memberID = args['memberID']
        self.productIDs = args['productIDs']
        self.productQuantities = args['productQuantities']
        self.approvalStatus = args['approvalStatus']
        self.transactionDate = args['transactionDate']

        self.pk = self.getID()
        return
