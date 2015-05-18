from Solution import Solution

solution = Solution()
print True, solution.isMatch('c', 'c*c')
print True, solution.isMatch('aa', 'aa')
print False, solution.isMatch('aa', 'b*')
print True, solution.isMatch('aa', 'a*')
print False, solution.isMatch('aa', 'a')
print True, solution.isMatch('ac', '.*c')
print True, solution.isMatch('accc', '.*')

