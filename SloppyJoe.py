#!/usr/bin/python
import random

class SloppyJoe(object):
	def __init__(self):
		self.adjectives = [x.rstrip() for x in open("words.txt").readlines()]
		self.names = [x.rstrip() for x in open("names.txt").readlines()]

	def get_adjective(self):
		return random.sample(self.adjectives, 1)[0]

	def common_name(self, names=[]):
		if len(names) == 0: names = self.names
		return random.sample(names, 1)[0]

	def generate_name(self, alliterate=False):
		adjective = self.get_adjective()

		if alliterate:
			names = []

			while len(names) == 0:
				adjective_first_char = adjective[0]
				names = filter(lambda x: x[0] == adjective_first_char, self.names)
				if len(names) == 0: adjective = self.get_adjective() # If there aren't any names, get a new adjective and try again.

		else:
			names = self.names
			adjective = self.get_adjective()

		name = self.common_name(names)
		return "%s %s" % (adjective, name)
