import pdb
class Solution:
	def __init__(self):
		self.level = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
	# @param {integer} num
	# @return {string}
	def intToRoman1(self, num):
		digits = []
		while num > 0:
			digits.append(num % 10)
			num /= 10
		result = []
		for i in range(len(digits)):
			if digits[i] > 0:
				d = digits[i]
				if d < 4:
					result.append(self.level[i*2]*d)
				if d == 4:
					result.append(self.level[i*2]+self.level[i*2+1])
				if d < 9 and d >= 5:
					result.append(self.level[i*2+1]+self.level[i*2]*(d%5))
				if d == 9:
					result.append(self.level[i*2]+self.level[i*2+2])
		result.reverse()
		return ''.join(result) 

	def intToRoman(self, num):
		result = []
		i = 0
		while num > 0:
			d = num % 10
			num /= 10
			if d > 0:
				twice = i*2
				if d < 4:
					result.append(self.level[twice]*d)
				if d == 4:
					result.append(self.level[twice]+self.level[twice+1])
				if d < 9 and d >= 5:
					result.append(self.level[twice+1]+self.level[twice]*(d%5))
				if d == 9:
					result.append(self.level[twice]+self.level[twice+2])
			i += 1
		result.reverse()
		return ''.join(result) 
