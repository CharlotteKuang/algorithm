import copy

class Solution:
	# @param {integer[]} candidates
	# @param {integer[]} combination 
	# @param {integer} target
	# @param {integer} total 
	# @return {integer[][]}
	def combination(self, candidates, combination, target, total):
		if total == target:
			result = []
			for num in combination:
				result.append(num)
			return [result]
		else:
			result = []
			for i in range(0, len(candidates)):
				if (i == 0 or candidates[i] != candidates[i-1] ) and candidates[i] + total <= target:
					combination.append(candidates[i])
					combs = self.combination(candidates[i+1:], combination, target, total + candidates[i])
					result += combs
					combination.pop()
			return result

	# @param {integer[]} candidates
	# @param {integer} target
	# @return {integer[][]}
	def combinationSum2(self, candidates, target):
		if not candidates:
			return []
		candidates.sort()
		return self.combination(candidates, [], target, 0)
