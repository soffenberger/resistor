import os
import sys
import cv2 as cv
import sqlite3 as sql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_sql_engine import *
from Tkinter import Tk
from tkFileDialog import askopenfilename

engine = create_engine('sqlite:///img.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class image(object):
	def __init__(self, name):
		self.name = name
		self.path = self.select_file()
		self.arr = self.gen_num_arr(self.path)

	def store_to_database(self):
		new_image = img(name = self.name, pt = self.path, array = self.arr)
		global session
		session.add(new_image)
		session.commit()
	def load_from_database(self, id):
		global session
		return session.query(img).filter(img.id == id)
 
	def gen_num_arr(self, path):
		return cv.imread(self.path)

	def select_file(self):
		root = Tk()
		root.withdraw()
		return askopenfilename()
