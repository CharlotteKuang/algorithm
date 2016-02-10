import pdb

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        sum_range = 0
        p = 0
        size = len(nums)
        rst = 0
        
        #pdb.set_trace()
        while sum_range < n:
            wanted_num = sum_range + 1
            if p < size:
                if nums[p] <= wanted_num:
                    sum_range = sum_range + min(wanted_num,nums[p])
                    p += 1
                else:
                    sum_range = sum_range + wanted_num
                    rst += 1
            else:
                rst += 1
                sum_range = sum_range + wanted_num
        return rst

if __name__ == "__main__":
    sol = Solution()

    case = [1,5,13]
    print case, sol.minPatches(case, 101)

    case = [1,3]
    print case, sol.minPatches(case, 101)

    case = [1,2,31,33]
    print case, sol.minPatches(case, 2147483647)

    case = [1,1,2,2]
    print case, sol.minPatches(case, 5)

    case = []
    print case, sol.minPatches(case, 10)
