from Solution import Solution

def main():
	solution = Solution()
	testCases = [
		[],
		['adfg'],
		['', '', ''],
		['abcd', 'abe', 'ab']
	]
	for test in testCases:
		print solution.longestCommonPrefix(test)

if __name__ == '__main__':
	main()
