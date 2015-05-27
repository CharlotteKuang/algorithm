from Solution import *

testCase = [
	[],
	[1,2],
	[1,2,3],
	[1,2,3,4,5,6],
	[1,2,3,4,5,6,7]
]

solution = Solution()
for test in testCase:
	l = makeList(test) 
	printList(solution.removeNthFromEnd(l, 2))
	print
