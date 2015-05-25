import pdb
class Solution:
	# @param {integer[]} height
	# @return {integer}
	def largestRectangleArea(self, height):
		height.append(0)
		stack = []
		maxArea = 0
		i = 0
        #pdb.set_trace()
		while i < len(height):
			if len(stack) > 0 and height[stack[-1]] > height[i]:
				cur = stack.pop(-1)
				if len(stack) == 0:
					maxArea = max(maxArea, height[cur] * i)
				else:
					maxArea = max(maxArea, height[cur] * (i-stack[-1]-1))
			else: 
				stack.append(i)
				i += 1
		return maxArea
