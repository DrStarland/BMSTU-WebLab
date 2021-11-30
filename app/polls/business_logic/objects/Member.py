#from django.core.exceptions import ValidationError
from .base import BusinessLogicObject
from django.urls import reverse

class Member_bl(BusinessLogicObject):
    def __init__(self, memberID=None, username=None, password=None, email=None,
        fullname=None, address=None, phone=None, args=None):
        if not args: 
            self.memberID = memberID
            self.username = username
            self.password = password
            self.email = email
            self.fullname = fullname
            self.address = address
            self.phone = phone
            self.pk = self.getID()
        else:
            self.updateFromDict(args)

    def __repr__(self):
        return f"<" + self.__class__.__name__ + f" {self.memberID}> " + " " + str(self.username)

    def getID(self):
        return self.memberID

    def get_absolute_url(self):
        #return "/Members/%i/" % self.getID()
        print("!!!!!!!!!!", reverse('application-detail', args=[str(self.getID())]))
        return reverse('application-detail', args=[str(self.getID())])

    def updateFromDict(self, args):
        self.memberID = args['memberID']
        self.username = args['username']
        self.password = args['password']
        self.email = args['email']
        self.fullname = args['fullname']
        self.address = args['address']
        self.phone = args['phone']
        self.pk = self.getID()
        return

