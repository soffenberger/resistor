import os
import sys
import sqlite3 as sql
import numpy as np
import io
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import *

Base = declarative_base()

class img(Base):
	__tablename__ = 'img'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False, unique=True)
	array = Column(BLOB, nullable=False)
	pt = (String(250))
	tru_false = Column(Boolean(name='bool'))


engine = create_engine('sqlite:///img.db')
Base.metadata.create_all(engine)
	
