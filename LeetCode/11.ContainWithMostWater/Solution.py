class Solution:
	# @param {integer[]} height
	# @return {integer}
	def maxArea(self, height):
		result = 0
		left = 0
		right = len(height) - 1
		while left < right:
			tmp = (right - left) * min(height[left], height[right])	
			if result < tmp:
				result = tmp
			if height[left] > height[right]:
				right -= 1
			else:
				left += 1
		return result
