from Solution import *

def makeList(arr):
	if not arr: return None
	head = ListNode(arr[0])
	p = head
	for num in arr[1:]:
		p.next = ListNode(num)
		p = p.next
	return head

def printList(head):
	p = head
	result = []
	while p is not None:
		result.append(str(p.val))
		p = p.next
	print ','.join(result)

if __name__ == '__main__':
	solution = Solution()
	testCases = [
		[1,2,3,3,2,1],
		[1,2,3,2,1],
		[1,2,1],
		[1,2],
		[1],
		[1,2,2],
		[1,2,2,1],
		[1,2,3,4,5,6,7,8]
	]

	for t in testCases:
		l = makeList(t)
		print solution.isPalindrome(l)
		printList(l)
