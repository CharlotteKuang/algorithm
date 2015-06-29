import pdb
class Solution:
	# @param {string} version1
	# @param {string} version2
	# @return {integer}
	def compareVersion(self, version1, version2):
		pos1, pos2 = 0, 0
		while pos1 < len(version1) or pos2 < len(version2):
			c1, c2 = pos1, pos2
			if c1 >= len(version1): v1 = 0
			else:
				while c1 < len(version1) and version1[c1] != '.': c1 += 1
				v1 = int(version1[pos1:c1])
			if c2 >= len(version2): v2 = 0
			else:
				while c2 < len(version2) and version2[c2] != '.': c2 += 1
				v2 = int(version2[pos2:c2])
			if v1 > v2: return 1
			if v2 > v1: return -1
			pos1 = c1 + 1
			pos2 = c2 + 1
		return 0

if __name__ == '__main__':
	solution = Solution()
	print solution.compareVersion('1', '1.1')
	print solution.compareVersion('1.0', '1.1')
	print solution.compareVersion('1.0', '1')
