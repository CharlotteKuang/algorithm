import pdb
class Solution(object):
	def removeDuplicateLetters(self, s):
		"""
		:type s: str
		:rtype: str
		""" 
		rst = []

		pos_map = {}
		l_str = len(s)
		for i in range(l_str):
			if not s[i] in pos_map:
				pos_map[s[i]] = [i]
			else:
				pos_map[s[i]].append(i)

		start_index = 0
		while True:
			smallest_index = l_str
			for letter in pos_map:
				if len(pos_map[letter]):
					smallest_index = min(pos_map[letter][-1], smallest_index)
			if smallest_index == l_str:
				break
			smallest_letter = '{'
			index = l_str
			for i in range(start_index, smallest_index+1):
				letter = s[i]
				if len(pos_map[letter]):
					if letter < smallest_letter:
						smallest_letter = letter
						index = i
						pos_map[letter].pop(0)
			pos_map[smallest_letter] = []
			rst.append(smallest_letter)
			start_index = index + 1

		return ''.join(rst)
if __name__ == '__main__':
	sol = Solution()

	print sol.removeDuplicateLetters('cbacdcbc')
	print sol.removeDuplicateLetters('babc')
	print sol.removeDuplicateLetters('abc')
	print sol.removeDuplicateLetters('aefebc')
	print sol.removeDuplicateLetters('')
