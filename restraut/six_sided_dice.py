__author__ = 'RongbingMiao'


import sys

"""
Implement a 6 sided die with weights on the sides, so that we don't have an even probability
distribution, but it is weighted by a list of weights passed in at construction time.
After a large number of iterations of throwing this die, the results should closely match the desired
distribution.
"""


class SixSidedWeightedDie(object):
    # NOTE: since these are weights on a probability distribution, these should sum to one, and the incoming array
    # should be of length 6. You should throw if either of these preconditions is false
	def __init__(self, weights):
		super(SixSidedWeightedDie, self).__init__()
		print("initializing...\n")

		print(weights)
		# TODO fill in
		# wtCount = sum(weights)
		# lenCount = len(weights)
		# print(wtCount)

		# if	wtCount == 1.0:
			# print("wtCount = %f\n" % wtCount)
		# else:
			# print("Total weights are not equal to 100%. Exit....")
			# sys.exit(0)

		# if lenCount == 6:
			 # print("lenCount = %d\n" % lenCount)
		# else:
			# print("It is not a 6-sided dice. Exit....")
			# sys.exit(0)



# Throw the die: this should produce a value in [1,6]
	def throw_die(self):
		# pass # TODO fill in
		return [randint(1,6) for _ in xrange(6)]


# weights = [.05, .10, .15, .2, .2, .2, 0.1]
# the_die = SixSidedWeightedDie(weights)