import numpy as np
import cv2 as cv
import tensorflow as tf
import sqlalchemy as sql
from Tkinter import Tk
from tkFileDialog import askopenfilename

class image(self):
	def __init__(self):
		self.path = self.select_file()
		self.arr = self.gen_num_arr(path)

	def store_to_database(self):

	def load_from_database(self):

	def gen_num_arr(self, path):
		return cv.imread(self.path)

	def select_file(self):
		Tk.withdraw()
		return askopenfilename()