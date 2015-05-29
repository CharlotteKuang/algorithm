import copy

class Solution:
	def __recursivePermute(self, nums, arr):
		if len(arr) == len(nums):
			self.result.append(copy.copy(arr))
		else:
			for i in range(len(nums)):
				if not self.visited[i]:
					arr.append(nums[i])
					self.visited[i] = True
					self.__recursivePermute(nums, arr)
					arr.pop()
					self.visited[i] = False 

	# @param {integer[]} nums
	# @return {integer[][]}
	def permute(self, nums):
		self.result = []
		self.visited = [False] * len(nums)
		self.__recursivePermute(nums, [])			
		return self.result
