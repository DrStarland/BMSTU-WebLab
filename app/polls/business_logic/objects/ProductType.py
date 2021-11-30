#from django.core.exceptions import ValidationError
from django.urls import reverse
from .base import BusinessLogicObject

class ProductType_bl(BusinessLogicObject):
    def __init__(self, typeID=None, typeName=None, description=None, args=None):
        if not args:
            self.typeID = typeID
            self.typeName = typeName
            self.description = description
            self.pk = self.getID()
        else:
            self.updateFromDict(args)

    def __repr__(self):
        return f"<" + self.__class__.__name__ + f" #{self.getID()}> " + " " + str(self.typeName) + ": " + str(self.description)

    def getID(self):
        return self.typeID

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.typeID)])

    def updateFromDict(self, args):
        self.typeID = args['typeID']
        self.typeName = args['typeName']
        self.description = args['description']

        self.pk = self.getID()
        return


