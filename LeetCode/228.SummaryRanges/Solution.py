class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		""" 
		if not nums: return []

		queue = [[nums[0]]]
		for n in nums[1:]:
			pre = queue[-1]
			if len(pre) == 1:
				if n == pre[0]+1:
					queue[-1].append(n)
				else:
					queue.append([n])
			else:
				if n == pre[1]+1:
					queue[-1][1] = n
				else:
					queue.append([n])
		return ['->'.join(str(r) for r in ran) for ran in queue] 

if __name__ == '__main__':
	case = [0,1,2,4,6,7,10,12,13]
	case = [0, 1]
	sol = Solution()
	print sol.summaryRanges(case)	
