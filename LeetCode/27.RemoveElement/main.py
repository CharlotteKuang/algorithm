from Solution import Solution

if __name__ == '__main__':
	testCases = [
		[[1,2,3,4,3,3,6,5,2], 3],
		[[1,3,4,5,6,7,8], 10],
	]
	solution = Solution()
	for test in testCases:
		print solution.removeElement(test[0], test[1])
		print test[0]
