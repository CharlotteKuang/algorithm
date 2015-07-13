class Solution:
	# @param {integer} n
	# @return {boolean}
	def isHappy(self, n):
		h = {}
		while True:
			sum_of_square = 0
			while n > 0:
				tmp = n % 10
				n /= 10
				sum_of_square += tmp * tmp
				if sum_of_square in h:
					return False
				else:
					h[sum_of_square] = True
				n = sum_of_square
				if n == 1: break
		return True
