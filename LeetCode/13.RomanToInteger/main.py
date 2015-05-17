from Solution import Solution

def main():
	solution = Solution()
	testCases = [
		'MCMXCVI',
		'I',
		'II',
		'III',
		'IV',
		'V',
		'VI',
		'VII',
		'VIII',
		'IX',
		'X',
		'CC',
		'MMM',
	]
	for test in testCases:
		print solution.romanToInt(test), test

if __name__ == '__main__':
	main()
