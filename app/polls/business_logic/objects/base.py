from abc import ABC, abstractmethod

class BusinessLogicObject(ABC):
    @abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.getID() == self.getID()

    def __hash__(self):
        return hash(self.getID())

    @abstractmethod
    def getID(self):
        raise NotImplementedError

    @abstractmethod
    def updateFromDict(self, args):
        raise NotImplementedError