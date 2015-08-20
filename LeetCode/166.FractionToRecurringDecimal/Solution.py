import pdb
class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		#pdb.set_trace()
		"""
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		sign = numerator * denominator >= 0
		if numerator < 0: numerator = -numerator
		if denominator < 0: denominator = -denominator
		arr = [str(numerator / denominator)]
		left = numerator % denominator
		result = ''
		if left:
			arr.append('.')
			remain = {} 
			count = 2
			while left:
				left *= 10
				if left in remain: break
				arr.append(str(left / denominator))
				remain[left] = count
				left = left % denominator
				count += 1
			if left: 
				pos = remain[left]
				result = ''.join(arr[0:pos]) + '(' + ''.join(arr[pos:]) + ')'
			else:
				result = ''.join(arr)
		else:
			result = ''.join(arr)
		if not sign: result = '-' + result
		return result
if __name__ == '__main__':
	sol = Solution()
	#wrong answer
	print sol.fractionToDecimal(0, 3)
	print sol.fractionToDecimal(1, 6)
	print sol.fractionToDecimal(7, -12)
	#wrong answer

	print sol.fractionToDecimal(1, 15)
	print sol.fractionToDecimal(1, 3)
	print sol.fractionToDecimal(2, 3)
	print sol.fractionToDecimal(20, 7)
	print sol.fractionToDecimal(5, 8)
