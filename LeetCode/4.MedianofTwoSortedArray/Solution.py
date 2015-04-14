import pdb
class Solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):
		#pdb.set_trace()
		m = len(A)
		n = len(B)
		if (m+n)%2:
			return self.findKthNumber(A, B, 0, m-1, 0, n-1, (m+n-1)/2)
		else:
			return (self.findKthNumber(A, B, 0, m-1, 0, n-1, (m+n-1)/2)
					+ self.findKthNumber(A, B, 0, m-1, 0, n-1, (m+n-1)/2+1))/2.0

	def findKthNumber(self, A, B, headA, tailA, headB, tailB, kth):
		#pdb.set_trace()
		if headA > tailA:
			return B[headB+kth]
		if headB > tailB:
			return A[headA+kth]

		midA = (headA+tailA)/2
		midB = (headB+tailB)/2
		midLength = midA-headA+midB-headB+2

		if A[midA] < B[midB]:
			if midLength-1 > kth:
				return self.findKthNumber(A, B, headA, tailA, headB, midB-1, kth)
			else:
				return self.findKthNumber(A, B, midA+1, tailA, headB, tailB, kth-(midA-headA+1))
		else:
			if midLength-1 > kth:
				return self.findKthNumber(A, B, headA, midA-1, headB, tailB, kth)
			else:
				return self.findKthNumber(A, B, headA, tailA, midB+1, tailB, kth-(midB-headB+1))
