# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy import ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

ENGINE=create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8", max_overflow=5)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'userinfo'

    id   = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return "<Person(name='%s')>" % self.name

Base.metadata.create_all(ENGINE)
Session = sessionmaker(bind=ENGINE)
# 往里面插入多条数据
session = Session()
session.add_all([
    Person(name='zhangli'),
    Person(name='li')
])
session.commit()
