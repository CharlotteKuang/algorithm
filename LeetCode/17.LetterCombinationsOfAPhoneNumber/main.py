from Solution import Solution

def main():
	testCases = [
		'',
		'23',
		'472'
	]
	solution = Solution()
	for test in testCases:
		print solution.letterCombinations(test)
	
if __name__ == '__main__':
	main()
