from Solution import Solution

def main():
	testCases = [
		'1',
		'-1',
		'00',
		'-922337203685477580723',
		'  f ',
		' 354 ',
		'   354 ',
		'   354',
		'',
		'   ',
		'  -0012a42', # return -12
		'2147483648',
	]
	solution = Solution()
	for test in testCases:
		print solution.myAtoi(test)


main()
