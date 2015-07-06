from Solution import Solution

if __name__ == '__main__':
	solution = Solution()
	testCases = [
		([2, 3, 6, 7], 7),
		([1, 2, 3, 6, 7], 7),
		([], 8),
		([2], 1),
	]

	for test in testCases:
		print solution.combinationSum(test[0], test[1])
