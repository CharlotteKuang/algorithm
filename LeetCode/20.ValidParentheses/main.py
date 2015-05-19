from Solution import Solution

def main():
	solution = Solution()
	testCases = ['(', ')', '{}', '{()[]}', '{([{}])}', '{()[']
	for test in testCases:
		print test, solution.isValid(test)


main()
