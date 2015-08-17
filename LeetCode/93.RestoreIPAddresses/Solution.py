import pdb
class Solution:
	def isIpCorrect(self, ip):
		return (len(ip) == 1 or ip[0] != '0') and 0 <= int(ip) <= 255
	def dfs(self, s, pos, ip):
		#pdb.set_trace()
		if pos == len(s) and len(ip) == 4: 
			self.result.append('.'.join(ip))
			return
		if pos == len(s) or len(ip) == 4: return
		for i in range(pos+1, len(s)+1):
			if self.isIpCorrect(s[pos:i]):
				t = ip + [s[pos:i]]
				self.dfs(s, i, t)
			else: break
	# @param {string} s
	# @return {string[]}
	def restoreIpAddresses(self, s):
		self.result = []
		self.dfs(s, 0, [])	
		return self.result
					        
if __name__ == '__main__':
	sol = Solution()

	print sol.restoreIpAddresses('25525511135')
	print sol.restoreIpAddresses('010010')
