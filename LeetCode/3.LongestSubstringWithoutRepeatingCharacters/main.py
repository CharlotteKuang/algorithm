def main():
	from Solution import Solution
	test = Solution() 
	testcases = ['abcabcbb', '', 'a', 'au', 'abba'] 
	for t in testcases:
		print test.lengthOfLongestSubstring(t)
main()
