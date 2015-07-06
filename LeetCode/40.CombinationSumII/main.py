from Solution import Solution

if __name__ == '__main__':
	solution = Solution()
	testCases = [
		([2, 3, 6, 7], 7),
		([1, 2, 3, 6, 7], 7),
		([], 8),
		([2], 1),
		([10,1,2,7,6,1,5], 8),
		([1,1,1,1,2], 4),
	]

	for test in testCases:
		print solution.combinationSum2(test[0], test[1])
