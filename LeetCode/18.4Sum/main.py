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
	print [-5,-4,-3,-2,-1,0,0,1,2,3,4,5], solution.fourSum([-5,-4,-3,-2,-1,0,0,1,2,3,4,5], 0)
	print [-1,0,1,2,-1,-4], solution.fourSum([-1,0,1,2,-1,-4], -1)
	print [-1,0,1,2,-1,-4,-1,2], solution.fourSum([-1,0,1,2,-1,-4], -1)
	for test in testCases:
		print test, ':', solution.fourSum(test, 0) 


if __name__ == '__main__':
	main()
