class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		""" 
		head, tail = 0, len(nums)-1
		while head < tail and head+1 < tail:
			mid = (head+tail)/2
			if target == nums[mid]: 
				return mid
			if target > nums[mid]: head = mid
			else: tail = mid

		if head > tail: return 0
		if head == tail: return max(head-1, 0) if target <= nums[head] else head+1
		if head+1 == tail: 
			if target <= nums[head]: return max(head-1, 0)
			if nums[head] < target <= nums[tail]: return head+1
			if target > nums[tail]: return tail+1

if __name__ == '__main__':
	sol = Solution()
	cases = [
		([1,3,5,6], 2),
		([1,3,5,6], 0),
		([1,3,5,6], 7),
		([1,3,5,6,10], 7),
		([], 7),
		([4], 7),
		([1,3], 1),
		([1,3,5,6], 5),
		([1,3], 3),
	]

	for case in cases:
		print sol.searchInsert(case[0], case[1])
