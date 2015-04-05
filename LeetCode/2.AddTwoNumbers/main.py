from addTwoNumbers import * 

def setListNode(array):
	result = None
	p = result
	for a in array:
		if result is None:
			result = ListNode(a)
			p = result
		else:
			p.next = ListNode(a)
			p = p.next
	return result 

def main():
	test = Solution()
	testCases = [
		([2,4,5], [5,6,4]),
		([],[]),
		([2,5,3,5], []),
		([], [2,5,3,5]),
		([1,3,5], [6,9,5,7,9]),
		# wrong answer:
		([5], [5]),
		([9, 8], [1])
	]
	for tc in testCases:
		ln1 = setListNode(tc[0]) 
		ln2 = setListNode(tc[1])
		print 'testCase result:'
		ln3 = test.addTwoNumbers(ln1, ln2)
		if ln3:
			ln3.getListNode()
		else:
			print 'None'

main()
