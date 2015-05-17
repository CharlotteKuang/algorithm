from Solution import Solution

def main():
	solution = Solution()
	testCases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 19, 20, 25, 27, 29, 40, 100, 101, 136, 569, 1357, 3999]
	for test in testCases:
		print test, solution.intToRoman(test)

if __name__ == '__main__':
	main()
