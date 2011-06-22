#!/usr/bin/python
import random


# A recipe generator? Have an ingredient associated with each name (would have to fewer names, and mostly ones of a specific ethnicity, and then have base recipes for the adjectives)

class SloppyJoe(object):
	def __init__(self):
		self.adjectives = [x.rstrip() for x in open("words.txt")]
		self.names = [x.rstrip() for x in open("names.txt")]

	def get_adjective(self):
		return random.sample(self.adjectives, 1)[0]

	def get_common_name(self, names=[]):
		if len(names) == 0: names = self.names
		return random.sample(names, 1)[0]

	def generate_name(self, alliterate=False):
		"""
		generate_name(alliterate=False) -> name

		Returns a name that is made from a list of synonyms for sloppy and common names.
		If alliterate is true will return only names where the adjective and the common name have the same first character.
		"""
		adjective = self.get_adjective()

		if alliterate:
			names = []

			while len(names) == 0:
				names = filter(lambda name: name[0] == adjective[0], self.names)
				if len(names) == 0: adjective = self.get_adjective() # If there aren't any names, get a new adjective and try again.

		else:
			names = self.names
			adjective = self.get_adjective()

		name = self.get_common_name(names)
		return "%s %s" % (adjective, name)
