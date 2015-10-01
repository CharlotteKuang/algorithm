import pdb
# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def __searchPosition__(self, numArr, num):
		#pdb.set_trace()
		top, tail = 0, len(numArr)-1
		while top+1 < tail:
			mid = (top+tail)/2
			if num == numArr[mid]:
				if mid % 2 == 0: return mid+1
				else: return mid
			if num < numArr[mid]:
				tail = mid
			else:
				top = mid
		if numArr[top] <= num <= numArr[tail]: return tail
		else:
			if num < numArr[top]: return top
			else: return tail+1

	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		""" 
		if len(intervals) == 0: return [newInterval]

		numArr = []
		for interval in intervals:
			numArr.append(interval.start)
			numArr.append(interval.end) 
		i = self.__searchPosition__(numArr, newInterval.start)
		j = self.__searchPosition__(numArr, newInterval.end)
		
		if i%2 == 0 and j%2 == 0:
			tmpInterval = newInterval
			overLapRange = (i/2, j/2)
		if i%2 == 0 and j%2 == 1:
			tmpInterval = Interval(newInterval.start, intervals[j/2].end)
			overLapRange = ((i+1)/2, (j+1)/2)
		if i%2 == 1 and j%2 == 0:
			tmpInterval = Interval(intervals[i/2].start, newInterval.end)
			overLapRange = (i/2, j/2)
		if i%2 == 1 and j%2 == 1:
			tmpInterval = Interval(intervals[i/2].start, intervals[j/2].end)
			overLapRange = (i/2, (j+1)/2)
		return intervals[0:overLapRange[0]] + [tmpInterval] + intervals[overLapRange[1]:]

if __name__ == '__main__':
	sol = Solution()
	#[1,2],[3,5],[6,7],[8,10],[12,16]
	case = [
		Interval(1,2),
		Interval(3,5),
		Interval(6,7),
		Interval(8,10),
		Interval(12,16),
	]
	#for i in range(-2, 25):
	#	print i, sol.searchPosition([1,2,3,5,6,7,8,10,12,16], i)
	rst = sol.insert(case, Interval(4, 9))
	for interval in rst:
		print interval.start, interval.end
	print 
	rst = sol.insert(case, Interval(0, 20))
	for interval in rst:
		print interval.start, interval.end
	print
	rst = sol.insert(case, Interval(-20, -4))
	for interval in rst:
		print interval.start, interval.end
	print
	rst = sol.insert(case, Interval(52, 59))
	for interval in rst:
		print interval.start, interval.end
