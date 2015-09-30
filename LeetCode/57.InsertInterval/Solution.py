import pdb
# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def __isConsistWithinInterval__(self, interval, num, isIncluded=True):
		if isIncluded:
			return interval.start <= num <= interval.end
		else:
			return interval.start < num < interval.end
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		""" 
		l = len(intervals)
		if l == 0: return [newInterval]
		if newInterval.end < intervals[0].start:
			return [newInterval] + intervals
		if newInterval.start > intervals[-1].end:
			return intervals + [newInterval]
		startOverlapIdx = -1
		endOverlapIdx = l
		startGapOverlapIdx = -1
		endGapOverlapIdx = l

		for i in range(l): 
			if self.__isConsistWithinInterval__(intervals[i], newInterval.start):
				startOverlapIdx = i
			else:
				if i < l-1:
					tmpInterval = Interval(intervals[i].end, intervals[i+1].start)
					if self.__isConsistWithinInterval__(tmpInterval, newInterval.start, False):
						startGapOverlapIdx = i
			if self.__isConsistWithinInterval__(intervals[i], newInterval.end):
				endOverlapIdx = i
				break
			else:
				if i < l-1:
					tmpInterval = Interval(intervals[i].end, intervals[i+1].start)
					if self.__isConsistWithinInterval__(tmpInterval, newInterval.end, False):
						endGapOverlapIdx = i
						break

		result = []
		pdb.set_trace()
		if 0 <= startOverlapIdx < l:
			for i in range(startOverlapIdx):
				result.append(intervals[i])
			if 0 <= endOverlapIdx  < l:
				result.append(Interval(intervals[startOverlapIdx].start, intervals[endOverlapIdx].end))
				for i in range(endOverlapIdx+1, l):
					result.append(intervals[i])
			else:
				tmpInterval = Interval(intervals[startOverlapIdx].start, newInterval.end)
				result.append(tmpInterval)
				for i in range(endGapOverlapIdx+1, l):
					result.append(intervals[i]) 
		else:
			for i in range(startGapOverlapIdx+1):
				result.append(intervals[i])
			if 0 <= endOverlapIdx  < l:
				result.append(Interval(newInterval.start, intervals[endOverlapIdx].end))
				for i in range(endOverlapIdx+1, l):
					result.append(intervals[i])
			else:
				result.append(newInterval)
				for i in range(endGapOverlapIdx+1, l):
					result.append(intervals[i]) 
		return result

if __name__ == '__main__':
	sol = Solution()
	intervals = [
		Interval(2,6),
		Interval(7,9),
	]
	newInterval = Interval(15,16)
	rst = sol.insert(intervals, newInterval)
	for interval in rst:
		print interval.start, interval.end
