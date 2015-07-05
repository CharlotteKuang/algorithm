from Solution import *

if __name__ == '__main__':
	solution = Solution()
	testCases = [
		[1,2,3,4],
		[0],
		[9,9],
		[9,9,9],
		[4,5,2,9,9],
	]

	for test in testCases:
		print solution.plusOne(test)
