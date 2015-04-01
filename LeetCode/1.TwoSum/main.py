class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target): 
		sums = {} 
		for i in range(len(num)):
			if (target-num[i]) in sums:
				return (sums[target-num[i]]+1, i+1)
			else:
				sums[num[i]] = i
		return (0,0)

def main():
	test = Solution()
	arr = [2,7,11,15]
	target = 9
	target = 22
	print test.twoSum(arr, target)

main()
