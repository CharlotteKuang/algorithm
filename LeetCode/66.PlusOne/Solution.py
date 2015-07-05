import pdb
class Solution:
	# @param {integer[]} digits
	# @return {integer[]}
	def plusOne(self, digits): 
		result = [(digits[-1]+1)%10]
		if digits[-1]+1 == 10:
			carry = 1
		else:
			carry = 0
		count = len(digits)-2
		while count >= 0:
			result.append((digits[count]+carry)%10)
			if digits[count]+carry == 10:
				carry = 1
			else:
				carry = 0
				break
			count -= 1
		if carry == 0:
			c = count-1
			while c >= 0:
				result.append(digits[c])
				c -= 1
		else:
			result.append(1)
		result.reverse()
		return result	
