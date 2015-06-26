from Solution import * 

if __name__ == '__main__':
	solution = Solution()
	f = open('test.txt')

	testCase = int(f.readline())
	for i in range(testCase):
		listNum = int(f.readline())
		lists = []
		for j in range(listNum):
			nums = f.readline()[0:-1]
			if nums: 
				l = makeList(nums.split(' '))
			else: l = None
			lists.append(l)

		mergedList = solution.mergeKLists(lists)	
		printList(mergedList)
			
