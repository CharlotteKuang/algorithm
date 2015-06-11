from Solution import Solution
testCase = [(-3,0,3,4,0,-1,9,2), (0, 0, 0, 0, -1, -1, 1, 1),(-2, -2, 2, 2, 3, 3, 4, 4),(-2, -2, 2, 2, -1, -1, 1, 1), (-2, -2, 2, 2, -1, 4, 1, 6)]
solution = Solution()
for i in testCase:
	print solution.computeArea(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
