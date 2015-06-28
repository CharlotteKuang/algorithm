from Solution import Solution

if __name__ == '__main__':
	tests = ['1-3*5-2', "282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024", "1*2-3/4+5*6-7*8+9/10", '0', '1+2', ' 4+ 4', '(1+2)', '(  4 - 4  -5)', '(-3+(4-5)-5)',
			'3+2*2+4/2-5',"100000000/1/2/3/4/5/6/7/8/9/10"]
	solution = Solution()
	for test in tests:
		print solution.calculate(test)
