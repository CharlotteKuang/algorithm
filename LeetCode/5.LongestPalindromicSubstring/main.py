from Solution import Solution

def main():
	testCases = [
		'cabbaccdcca',
		't4g4tg'
	]
	solution = Solution()
	for t in testCases:
		print solution.longestPalindrome(t)

if __name__ == '__main__':
	main()
