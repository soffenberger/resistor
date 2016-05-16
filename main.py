#!/usr/bin/python
from create_sql_engine import *
import resistor_class as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///img.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def load_from_database_id(id):
	global session
        return session.query(img).filter(img.id == id).all()

def main():
	im = load_from_database_id(int(1))
	global session
	image = session.query(img).first()
	for i in im:
		print i.name
	print image.name


if __name__ == '__main__':
	print "Fuck Frank"
	main()
