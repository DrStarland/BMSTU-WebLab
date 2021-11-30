from django.db.models.query import QuerySet, MAX_GET_RESULTS

import copy
import operator
import warnings
from itertools import chain

import django
from django.conf import settings
from django.core import exceptions
from django.db import (
    DJANGO_VERSION_PICKLE_KEY, IntegrityError, NotSupportedError, connections,
    router, transaction,
)
from django.db.models import AutoField, DateField, DateTimeField, sql
from django.db.models.constants import LOOKUP_SEP
from django.db.models.deletion import Collector
from django.db.models.expressions import Case, Expression, F, Ref, Value, When
from django.db.models.functions import Cast, Trunc
from django.db.models.query_utils import FilteredRelation, Q
from django.db.models.sql.constants import CURSOR, GET_ITERATOR_CHUNK_SIZE
from django.db.models.utils import create_namedtuple_class, resolve_callables
from django.utils import timezone
from django.utils.functional import cached_property, partition

class MyQuerySet(QuerySet):
    charged = False
    data = None

    def is_charged(self):
        return self.charged

    def special_upload(self, data_dict):
        self.data = data_dict[:]
        self.charged = True
        return True

    def _alive_(self):
        print("Ya zhivoy")

    # def get(self, *args, **kwargs):
    #     """
    #     Возвращает новый QuerySet содержащий объекты отвечающие параметрам фильтрации.
    #     Параметры фильтрации (**kwargs) должны отвечать формату описанному в соответствующем
    #     разделе. Несколько параметров объединяются оператором SQL AND.
    #     """
    #     # result = list()
    #     # # да, это неправильная и плохая реализация, но это временно
    #     # # чисто для доказательства самой возможности
    #     # while kwargs:
    #     #     filter_key, filter_value = kwargs.popitem()
    #     #     for elem in self.data:
    #     #         if elem[filter_key] == filter_value:
    #     #             result.append(elem)

    #     # return result
    #     return super().get(*args, **kwargs)
    # from django.core import exceptions
    # def get(self, *args, **kwargs):
    #     """
    #     Perform the query and return a single object matching the given
    #     keyword arguments.
    #     """
    #     if self.query.combinator and (args or kwargs):
    #         raise NotSupportedError(
    #             'Calling QuerySet.get(...) with filters after %s() is not '
    #             'supported.' % self.query.combinator
    #         )
    #     clone = self._chain() if self.query.combinator else self.filter(*args, **kwargs)
    #     if self.query.can_filter() and not self.query.distinct_fields:
    #         clone = clone.order_by()
    #     limit = None
    #     if not clone.query.select_for_update or connections[clone.db].features.supports_select_for_update_with_limit:
    #         limit = MAX_GET_RESULTS
    #         clone.query.set_limits(high=limit)
    #     num = len(clone)
    #     if num == 1:
    #         return clone._result_cache[0]
    #     if not num:
    #         raise self.model.DoesNotExist(
    #             "%s matching query does not exist." %
    #             self.model._meta.object_name
    #         )
    #     raise self.model.MultipleObjectsReturned(
    #         'get() returned more than one %s -- it returned %s!' % (
    #             self.model._meta.object_name,
    #             num if not limit or num < limit else 'more than %s' % (limit - 1),
    #         )
    #     )
    
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)

    def __len__(self) -> int:
        return False

    # def __repr__(self) -> str:
    #     return "Nechego tut repr delat"



#test = QuerySet.filter