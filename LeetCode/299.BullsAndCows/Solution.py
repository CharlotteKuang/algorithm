import pdb
class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		l = len(secret)
		acount = 0
		bcount = 0
		posHash = {}
		for i in range(l):
			if not secret[i] in posHash:
				posHash[secret[i]] = {}
			posHash[secret[i]][i] = True
		pdb.set_trace()
		for j in range(l):
			if secret[j] == guess[j]:
				acount += 1
				del(posHash[secret[j]][j])
		for j in range(l):
			if secret[j] != guess[j] and guess[j] in posHash and posHash[guess[j]]:
				bcount += 1
				for pos in posHash[guess[j]]:
					del(posHash[guess[j]][pos])
					break
		return '%dA%dB' % (acount, bcount)

if __name__ == '__main__':
	sol = Solution()
	print sol.getHint('11', '10')
