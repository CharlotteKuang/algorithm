from Solution import Solution

def main():
	solution = Solution()
	testCases = [
		1,
		139646931,
		13966931,
		10,
		121,
		100,
		145,
		31221,
	]
	for test in testCases:
		print solution.isPalindrome(test)

main()
