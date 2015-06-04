from Solution import * 

def main():
	solution = Solution()
	testCases = [
		[],
		[1,2],
		[1,2,3],
		[1,2,3,4],
		[1,2,3,4,5],
		[1,2,3,4,5,6],
	]	
	for t in testCases:
		p = solution.swapPairs(makeList(t))
		printList(p)

main()
