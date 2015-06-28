from Solution import Solution

if __name__ == '__main__':
	tests = ['1+2', ' 4+ 4', '(1+2)', '(  4 - 4  -5)', '(-3+(4-5)-5)']
	solution = Solution()
	for test in tests:
		print solution.calculate(test)
