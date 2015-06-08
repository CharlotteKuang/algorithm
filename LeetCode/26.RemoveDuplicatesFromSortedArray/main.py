from Solution import Solution

if __name__ == '__main__':
	testCases = [
		[1,3,3,3,4,5,6,7,7,7,9,10],
		[1,3,4,5,6,7,8],
	]
	solution = Solution()
	for test in testCases:
		test.sort()
		print solution.removeDuplicates(test)
		print test
