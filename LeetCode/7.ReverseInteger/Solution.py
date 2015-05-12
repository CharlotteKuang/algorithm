import pdb
import sys
class Solution:
	# @param {integer} x
	# @return {integer}
	def reverse(self, x):
		# not working~~
		sign = 1
		if x < 0:
			sign = -1
			x = -x
		result = 0
		while x > 0:
			if result > sys.maxint:
				return 0
			result = result * 10 + x % 10
			x /= 10
		return sign * result 
