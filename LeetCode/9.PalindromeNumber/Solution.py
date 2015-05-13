import pdb
class Solution:
	# @param {integer} x
	# @return {boolean}
	def isPalindrome(self, x):
		if x < 0: return False
		if 0 <= x < 10: return True
		#extract the half of the integer
		#the integer ends with 0 must not be a palindromic number
		if x % 10 == 0: return False
		top = x
		tail = 0
		while top > tail:
			tail = tail * 10 + top % 10
			top /= 10
		if top == tail: return True
		if top == tail / 10 : return True
		else: return False
