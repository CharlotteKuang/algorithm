import pdb
class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		""" 
		# non-trival case
		if not len(nums): return [-1, -1]
		
		#pdb.set_trace()
		head, tail = 0, len(nums)
		while head < tail:
			mid = (head+tail)/2
			if target > nums[mid]: head = mid+1
			else: tail = mid
		if head > tail: return [-1, -1]
		else: 
			if head < len(nums) and nums[head] == target:
				pre = head-1
				while pre >= 0 and nums[pre] == target: pre -= 1
				post = head+1
				while post < len(nums) and nums[post] == target: post += 1
				return [pre+1, post-1]	
			return [-1,-1]
if __name__ == '__main__':
	sol = Solution()
	print sol.searchRange([2], 1)
	a = [5,7,7,8,8,10]
	print sol.searchRange(a, 11)
	for i in range(0, 12):
		print i, sol.searchRange(a, i)
	a = [5,7,14,29,42,42,47]
	for i in range(0, 12):
		print i, sol.searchRange(a, i)
