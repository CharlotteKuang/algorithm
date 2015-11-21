import pdb
class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		""" 
		# eg: 123 * 456
		count = len(num1) + len(num2) + 1
		cal = [0 for i in range(count)]

		mul1 = [int(s) for s in num1]
		mul2 = [int(s) for s in num2]
		
		start = count - 1
		#pdb.set_trace()
		for i in range(len(mul2) - 1, -1, -1):
			m2 = mul2[i]
			p = start
			if m2 != 0:
				carry = 0
				for j in range(len(mul1) - 1, -1, -1):
					m1 = mul1[j]
					tmp = m1 * m2
					mul = tmp % 10
					sum_up = cal[p] + mul + carry
					carry = sum_up / 10 + tmp / 10
					cal[p] = sum_up % 10
					p -= 1
				cal[p] = carry
			start -= 1

		non_zero_pos = 0
		while non_zero_pos < count and cal[non_zero_pos] == 0:
			non_zero_pos += 1

		return ''.join([str(i) for i in cal[non_zero_pos:]]) if non_zero_pos < count else "0"

if __name__ == '__main__':
	cases = [("123", "456"), ("0", "0"), ("99", "99"), ("10", "32")]

	sol = Solution()

	for case in cases:
		print sol.multiply(case[0], case[1])
