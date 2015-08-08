import pdb
class Solution:
	# @param {integer} n
	# @return {integer}
	def countPrimes(self, n):
		if n <= 2: return 0

		a = [True] * (n+1)
		a[0] = a[1] = False
		a[2] = True
		count = 0 
		for i in range(2, n/2+1):
			if not a[i]: continue
			base = i*i
			while base < n:
				a[base] = False
				base += i
		
		for i in range(2, n): 
			count += a[i]
		return count

if __name__ == '__main__':
	solution = Solution()
	num = 1500000 
	print solution.countPrimes(num)

	num = 499979 
	print solution.countPrimes(num)

	num = 3 
	print solution.countPrimes(num)

	num = 2 
	print solution.countPrimes(num)

	num = 4 
	print solution.countPrimes(num)

	num = 5 
	print solution.countPrimes(num)

	num = 6 
	print solution.countPrimes(num)

	num = 8 
	print solution.countPrimes(num)

	num = 10 
	print solution.countPrimes(num)
