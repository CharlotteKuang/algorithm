class Solution(object):
	def isNumber(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		
		pos, l = 0, len(s)
		
		if l == 0: return False
		
		while pos < l and s[pos] == ' ':
			pos += 1
			
		if pos == l: return False
		
		if s[pos] in ['+', '-']: pos += 1
		
		if pos == l: return False
		
		flag1 = False
		while pos < l and s[pos] in numbers:
			pos += 1
			flag1 = True
			
		flag2 = False	
		if pos  < l and s[pos] == '.':
			pos += 1
			while pos < l and s[pos] in numbers:
				pos += 1
				flag2 = True
			if not flag1 and not flag2: return False
				
		if pos < l and s[pos] in ['e', 'E']:
			if not flag1 and not flag2: return False
			pos += 1
			
			if pos < l and s[pos] in ['+', '-']: pos += 1
			
			flag3 = False
			while pos < l and s[pos] in numbers:
				pos += 1
				flag3 = True
			if not flag3: return False 
		
		while pos < l and s[pos] == ' ':
			pos += 1
			
		return pos == l
if __name__ == '__main__':
	sol = Solution()
	cases = [
		" 005047e+6",
		".2e81",
		"6e6.5",
		"1e.66",
		"3.",
		".1",
		"bfskj",
		"3e",
		"",
		"1",
		"  0.1   ",
		" 4.325E135",
	]
	for case in cases:
		print sol.isNumber(case)
