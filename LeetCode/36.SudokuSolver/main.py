from Solution import Solution

if __name__ == '__main__':
	solution = Solution()

	for i in range(2):
		f = open('test' + str(i) + '.txt')
		case = [(line[0:-1]).split(' ') for line in f.readlines()] 
		f.close()
		
		solution.solveSudoku(case)
		result = open('result' + str(i) + '.txt', 'w')
		for row in case:
			result.write(' '.join(row) + '\n')
		result.close() 
