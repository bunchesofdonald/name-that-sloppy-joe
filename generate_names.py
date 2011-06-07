#!/usr/bin/python

from SloppyJoe import SloppyJoe

sj = SloppyJoe()

for _ in xrange(10):
	print sj.generate_name(alliterate=True)
