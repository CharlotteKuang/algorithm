from Solution import Solution

def main():
	solution = Solution()
	testCase = [
		([1,2,4,8,16,32,64,128], 82),
		([1,1,1,0], -100),
		([-1,2,1,-4], 1),
	]
	for test in testCase:
		print solution.threeSumClosest(test[0], test[1])

if __name__ == '__main__': main()
