from typing import Set
import abc

class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    def add(self, entity):
        self.seen.discard(entity)
        self.seen.add(entity)

    def delete(self, entity):
        self.seen.discard(entity)

    def get(self, entID):
        p = self._get(entID)
        if p:
            self.seen.add(p)
        return p

    @abc.abstractmethod
    def _get(self, entID):
        raise NotImplementedError


class DjangoRepository(AbstractRepository):
    django_model = None

    def add(self, bl_object):
        super().add(bl_object)
        self._update(bl_object)
        
    def _update(self, bl_object):
        self.django_model.update_from_domain(bl_object)

    def update(self, bl_object):
        return self.add(bl_object)

    def create(self, bl_object):
        return self.add(bl_object)

    def delete(self, bl_object):
        super().delete(bl_object)
        self.django_model.objects.filter(pk = bl_object.getID()).delete()

    def _get(self, ID):
        source =  self.django_model.objects.filter(pk = ID).first()
        if source is not None:
            return ( source.to_domain() )
        else:
            return None

    def list(self):
        return [b.to_domain() for b in self.django_model.objects.all()]

# подключение объекта бизнес логики не требуется, оставлено для наглядности
# from ..business_logic.objects import Product as prod_bl
from ..modelsDB.Product import Product as prod_DB
class DjangoRepository_Product(DjangoRepository):
    django_model = prod_DB


#from ..business_logic.objects import ProductType as prodType_bl
from ..modelsDB.Product import ProductType as prodType_DB

class DjangoRepository_ProductType(DjangoRepository):
    django_model = prodType_DB


from ..modelsDB.Cart import Cart as cart_DB

class DjangoRepository_Cart(DjangoRepository):
    django_model = cart_DB


from ..modelsDB.Comment import Comment as comm_DB

class DjangoRepository_Comment(DjangoRepository):
    django_model = comm_DB


from ..modelsDB.Member import Member as member_DB

class DjangoRepository_Member(DjangoRepository):
    django_model = member_DB


from ..modelsDB.Rating import Rating as rating_DB

class DjangoRepository_Rating(DjangoRepository):
    django_model = rating_DB


from ..modelsDB.Transaction import Transaction as transaction_DB

class DjangoRepository_Transaction(DjangoRepository):
    django_model = transaction_DB

        