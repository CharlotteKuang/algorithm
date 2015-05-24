from Solution import Solution

def main():
	testCases = [
		[1,1,-1,-1,-1,0,0,0],
		[-1,0,1,2,-1,-4],
		[-1,0,1,2,-1,-4,4,4],
		[1,3],
		[],
	]

	solution = Solution()
	for test in testCases:
		print test, ':', solution.threeSum(test)


if __name__ == '__main__':
	main()
