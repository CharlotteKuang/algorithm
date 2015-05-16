from Solution import Solution

def main():
	solution = Solution()
	testCases = [
		[1],
		[],
		[5,2,6,7,4,5,8,2],
		[1,2,3,4,5,6,7,8,9]
	]
	for test in testCases:
		print solution.maxArea(test)

main()
