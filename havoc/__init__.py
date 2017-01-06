# -*- coding: utf-8 -*-

import decimal
import datetime

import faker

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    class_mapper,
    make_transient,
    scoped_session,
    sessionmaker)

from sqlalchemy import exc, func, select
from sqlalchemy.dialects.postgresql import ARRAY, HSTORE, UUID

from sqlalchemy.orm.properties import (
    RelationshipProperty,
    SynonymProperty)
from sqlalchemy.orm.query import Query
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.sql.expression import true
from sqlalchemy_utils.types import TSVectorType

from sqlalchemy_searchable import make_searchable, parse_search_query
from sqlalchemy_utils.expressions import tsvector_match, to_tsquery

from zope.sqlalchemy import ZopeTransactionExtension


from familias.models.auth import Usuario

'''
generators = {
    bool: faker.pybool,
    float: faker.pyfloat,
    int: faker.random_int,
    str: faker.pystr,
    bytes: faker.pybytes,
    list: faker.pylist,
    set: faker.pyset,
    tuple: faker.pytuple,
    dict: faker.pydict,
    datetime.date: faker.date,
    datetime.datetime: faker.date_time,
    datetime.time: faker.time,
    decimal.Decimal: faker.pydecimal,
    t.BigInteger: faker.big_integer,
    t.EmailString: faker.email,
    t.HostnameString: faker.domain_name,
    t.IP4String: faker.ipv4,
    t.IP6String: faker.ipv6,
    t.IPString: faker.ip_generic,
    t.NullOrBoolean: faker.null_boolean,
    t.PositiveDecimal: faker.positive_decimal,
    t.PositiveInteger: faker.positive_integer,
    t.PositiveSmallInteger: faker.small_positive_integer,
    t.SmallInteger: faker.small_integer,
    t.Text: faker.text,
    t.URL: faker.url,
    t.UUID: faker.uuid,
    type(None): '',
}

fakers = {
    ('address', str): faker.street_address,
    ('body', str): faker.text,
    ('category', str): faker.genre,
    ('city', str): faker.city,
    ('company', str): faker.company,
    ('content', str): faker.text,
    ('country', str): faker.country,
    ('description', str): faker.text,
    ('domain', str): faker.domain_name,
    ('email', str): faker.email,
    ('first_name', str): faker.first_name,
    ('firstname', str): faker.first_name,
    ('genre', str): faker.genre,
    ('last_name', str): faker.last_name,
    ('lastname', str): faker.last_name,
    ('lat', float): faker.latitude,
    ('latitude', float): faker.latitude,
    ('login', str): faker.user_name,
    ('lon', float): faker.longitude,
    ('longitude', float): faker.longitude,
    ('name', str): faker.name,
    ('percent', decimal.Decimal): faker.percent_decimal,
    ('percent', int): faker.percent,
    ('phone', str): faker.phone_number,
    ('site', str): faker.url,
    ('slug', str): faker.slug,
    ('street', str): faker.street_name,
    ('time_zone', str): faker.timezone,
    ('timezone', str): faker.timezone,
    ('title', str): faker.title,
    # ('url', t.URL): faker.uri,
    ('url', str): faker.uri,
    ('username', str): faker.user_name,
}
'''


class SqlAlchemy(object):
    def __init__(self, *ag, **kw):
        pass

    def map_columns(self, cls, foreign_keys=False, skip_fields=[]):
        d = {}
        fks = []
        if not foreign_keys:
            fks = [fk.parent.key for fk in cls.__table__.foreign_keys]

        not_classes = (RelationshipProperty, SynonymProperty)
        for column in cls.__table__.columns:
            if (column.key in fks or
                    column.key in skip_fields or
                    isinstance(column, not_classes) or
                    column.key.startswith('_sa')):
                continue
            if callable(column.default):
                column.default()
            d[column.key] = (column, column.default)
        return d

    def supply(self, cls):
        '''
        Generates a populated sqlalchemy object using `cls`.
        '''
        columns = self.map_columns(cls)

        return columns
        # return obj


havoc = SqlAlchemy()
user = havoc.supply(Usuario)

for k, v in user.items():
    print(k, v)
