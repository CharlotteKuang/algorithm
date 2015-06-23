from Solution import *

if __name__ == '__main__':
	solution = Solution()

	s1, s2, s3 = "ab", "bc", "babc" 
	print solution.isInterleave(s1, s2, s3) 

	s1 = "aabcc"
	s2 = "dbbca" 
	s3 = "aadbbcbcac"
	s3 = "aadbbbaccc"
	
	print solution.isInterleave(s1, s2, s3)

	s1 = "aabc"
	s2 = "dbbca" 
	s3 = "aadbbcbca"
	
	print solution.isInterleave(s1, s2, s3)

	s1, s2, s3 = "db", "b", "cbb"
	print solution.isInterleave(s1, s2, s3) 
