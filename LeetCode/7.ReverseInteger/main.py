from Solution import Solution

def main():
	solution = Solution()
	testCases = [
		#0,
		#123,
		#-123,
		192233720368547758071,
		1000000003,
		#10,
		#1000,
	]
	for test in testCases:
		print solution.reverse(test)
main()
