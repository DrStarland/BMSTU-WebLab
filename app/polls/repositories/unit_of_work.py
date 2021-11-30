from __future__ import annotations
import abc
from django.db import transaction
from .repository import *


class AbstractUnitOfWork(abc.ABC):
    stored_model: AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError



class DjangoUnitOfWork(AbstractUnitOfWork):
    stored_model = None

    def __enter__(self):
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        transaction.set_autocommit(True)

    def commit(self):
        for prod in self.stored_model.seen:
            self.stored_model._update(prod)
        transaction.commit()

    def rollback(self):
        transaction.rollback()


class DjangoUnitOfWork_Product(DjangoUnitOfWork):
    stored_model = DjangoRepository_Product()

class DjangoUnitOfWork_ProductType(DjangoUnitOfWork):
    stored_model = DjangoRepository_ProductType()
    
class DjangoUnitOfWork_Cart(DjangoUnitOfWork):
    stored_model = DjangoRepository_Cart()

class DjangoUnitOfWork_Comment(DjangoUnitOfWork):
    stored_model = DjangoRepository_Comment()

class DjangoUnitOfWork_Member(DjangoUnitOfWork):
    stored_model = DjangoRepository_Member()

class DjangoUnitOfWork_Rating(DjangoUnitOfWork):
    stored_model = DjangoRepository_Rating()

class DjangoUnitOfWork_Transaction(DjangoUnitOfWork):
    stored_model = DjangoRepository_Transaction()
