# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
	def __str__(self):
		return '%d, %d' % (self.start, self.end)
class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		""" 
		if len(intervals) == 0: return []
		intervals = sorted(intervals, key=lambda x: x.start)
		#for interval in intervals:
		#	print interval
		rst = [intervals[0]]
		for interval in intervals[1:]: 
			if interval.start > rst[-1].end:
				rst.append(interval)
			else:
				if interval.end > rst[-1].end:
					rst[-1].end = interval.end
		return rst 

if __name__ == '__main__':
	case = [[1,3],[8,10],[2,6],[15,18]]
	intervals = []
	for interval in case:
		intervals.append(Interval(interval[0], interval[1]))	
	sol = Solution()
	rst = sol.merge(intervals)
	for interval in rst:
		print interval
