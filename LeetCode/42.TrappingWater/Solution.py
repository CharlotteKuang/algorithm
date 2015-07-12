class Solution:
	# @param {integer[]} height
	# @return {integer}
	def trap(self, bars):
		if not bars or len(bars) < 3:
			return 0
		volume = 0
		left, right = 0, len(bars) - 1
		l_max, r_max = bars[left], bars[right]
		while left < right:
			l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
			if l_max <= r_max:
			#is l_max is not bigger than r_max, then it is safe to add volume(l_max - bars[left]) because there is a safe boundary on the right.
				volume += l_max - bars[left]
				left += 1
			else:
				volume += r_max - bars[right]
				right -= 1
		return volume

solution = Solution()
print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print solution.trap([0,1,2])
