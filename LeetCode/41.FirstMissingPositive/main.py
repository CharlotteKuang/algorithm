from Solution import Solution

if __name__ == '__main__':
	tests = [[2], [1,1], [1,2,3,4], [4,2,1,3], [], [5,-1,4,2,1]]
	solution = Solution()
	for test in tests:
		print solution.firstMissingPositive(test)
		print test
