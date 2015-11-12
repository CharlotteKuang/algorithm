import pdb
class Solution(object):
	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		""" 
		oneArr = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'] 
		tenArr = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

		hundredArr = ['', 'One Hundred', 'Two Hundred', 'Three Hundred', 'Four Hundred', 'Five Hundred', 'Six Hundred', 'Seven Hundred', 'Eight Hundred', 'Nine Hundred'] 
		tenthArr = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

		notation = ['', 'Thousand', 'Million', 'Billion'] 

		if num == 0: return 'Zero' 

		notationCount = 0
		rst = []
		#pdb.set_trace()
		while num > 0:
			t = num % 1000
			num /= 1000
			
			section = []

			tmp = t / 100
			if tmp:
				section.append(hundredArr[tmp])
				t -= tmp * 100
			if 10 <= t <= 19:
				section.append(tenthArr[t % 10])
			else:
				tmp = t / 10
				if tmp:
					section.append(tenArr[tmp])
					t -= tmp * 10
				if t:
					section.append(oneArr[t])
			if section:
				if notationCount > 0:
					section.append(notation[notationCount])
				rst.insert(0, ' '.join(section))

			notationCount += 1

		return ' '.join(rst)

if __name__ == '__main__':
	sol = Solution()

	cases = [1000000, 0, 1, 2, 53, 613, 26, 756, 100, 1000, 53376, 4865224, 560000]
	for case in cases:
		print case, sol.numberToWords(case), 'X'
