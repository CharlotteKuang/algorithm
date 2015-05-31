import pdb 
class Solution:
	def __recursivePermute(self, nums, arr):
		if len(arr) == len(nums):
			tmp = [n for n in arr]
			self.result.append(tmp)
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

	def __recursivePermuteUnique(self, nums, arr):
		#pdb.set_trace()
		if len(arr) == len(nums):
			tmp = [n for n in arr]
			self.result2.append(tmp)
		else:
			for i in range(len(nums)):
				if i > 0 and nums[i] == nums[i-1] and not self.visited2[i-1]:
					continue
				if not self.visited2[i]:
					arr.append(nums[i])
					self.visited2[i] = True
					self.__recursivePermuteUnique(nums, arr)
					arr.pop()
					self.visited2[i] = False 

	# @param {integer[]} nums
	# @return {integer[][]}
	def permuteUnique(self, nums):
		nums.sort()
		self.result2 = []
		self.duplicate = [0] * len(nums)
		self.visited2 = [False] * len(nums)
		for i in range(1, len(nums)):
			if nums[i] == nums[i-1]:
				self.duplicate[i] = self.duplicate[i-1]+1
		self.__recursivePermuteUnique(nums, [])			
		return self.result2
