#!/usr/bin/python3
""" This module contains storage handling class """

import json
import os

class FileStorage():
	"""docstring for FileStorage"""

	def __init__(self):
		"""docstring for init method of FileStorage"""

		self.__file_path = "file.json"
		self.__objects = dict()

	def all(self):
		""" returns all objects in file """

		return (self.__objects)

	def new(self, obj):
		""" adds new object to dict """

		key = obj.__class__.__name__ + "." + obj.id
		self.__objects[key] = obj

	def save(self):
		""" serializes __objects to the JSON file """
		with open(self.__file_path, "w") as file:
			new_dict = {}
			for key, value in self.__objects.items():
				new_dict[key] = value.to_dict()
			json_text = json.dumps(new_dict)
			file.write(json_text)

	def reload(self):
		""" reloads all objects from file """

		from models.base_model import BaseModel
		if os.path.isfile(self.__file_path):
			with open(self.__file_path, 'r') as file:
				json_data = json.load(file)
			for kwar in json_data.values():
				cl = kwar["__class__"]
				cl = eval(cl)
				self.new(cl(**kwar))