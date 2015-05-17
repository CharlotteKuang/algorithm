import pdb 
class Solution:
	def __init__(self):
		self.level = {
			'I': 0,
			'V': 1,
			'X': 2,
			'L': 3,
			'C': 4,
			'D': 5,
			'M': 6,
		}
		self.value = {
			'I': 1,
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500,
			'M': 1000,
		}
		self.chars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
	# @param {string} s
	# @return {integer}
	def romanToInt(self, s):
		result = 0
		i = 0
		length = len(s)
        #pdb.set_trace()
		while i < length:
			c = s[i]
			if self.level[c]%2==0:
				#test if number is between 1 to 3
				j = i
				while j+1 < length and s[j+1]==c:
					j += 1
				if j != i:
					result += self.value[c]*(j-i+1)
					i = j+1
				else:
					#test if number is 4
					if c != 'M' and i+1 < length and s[i+1]==self.chars[self.level[c]+1]:
						result += self.value[c]*4
						i = i+2	
					#test if number is 9
					else:
						if c != 'M' and i+1 < length and s[i+1]==self.chars[self.level[c]+2]:
							result += self.value[c]*9
							i = i+2	
						else:
							result += self.value[c]
							i += 1
			else:
				#test if number is between 5 to 9
				j = i
				while j+1 < length and s[j+1]==self.chars[self.level[c]-1]:
					j += 1
				if j != i:
					c2 = self.chars[self.level[c]-1]
					result += self.value[c]+self.value[c2]*(j-i)
				else:
					result += self.value[c]
				i = j+1
		return result
