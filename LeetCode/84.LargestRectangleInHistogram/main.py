from Solution import Solution

def main():
	solution = Solution()
	testCase = [
		[6,2,5,4,5,1,6]
	]
	for test in testCase:
		print solution.largestRectangleArea(test)

if __name__ == '__main__':
	main()
