from Solution import Solution

def main():
	test = Solution()
	testcase = [
		([4,8,9,13,17,26], [3,6,10,18,21,28,33]),
		([], [2,3])
	]
	for t in testcase:
		print test.findMedianSortedArrays(t[0], t[1])

main()
