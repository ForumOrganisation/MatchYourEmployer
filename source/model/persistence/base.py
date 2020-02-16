# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# to change with the real database url
engine = create_engine('postgres://vqmqeszqdyzszc:04dbfdc35f85eef330cdb5a286ba4956ee987976dcdb72a8d830080e18fea896@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d8v8b30qua7c26')
Session = sessionmaker(bind=engine)

Base = declarative_base()
