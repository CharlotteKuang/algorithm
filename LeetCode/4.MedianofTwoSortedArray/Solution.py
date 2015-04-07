class Solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):
		length = len(A) + len(B)
		if length % 2:
			return self.findKthNumber(A, B, 0, m-1, 0, n-1, length/2)
		else:
			return (self.findKthNumber(A, B, length/2) + self.findKthNumber(A, B, length/2+1)) / 2

	def findKthNumber(self, A, B, topA, tailA, topB, tailB, k):
