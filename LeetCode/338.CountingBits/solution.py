import sys

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """ 
        if num == 0: return [0]

        bit_mark = 1
        dp = [0,1]
        
        pos = 1
        while pos < num: 
           next_num = pos+1
           if next_num == bit_mark<<1:
               dp.append(1)
               bit_mark <<= 1
           else:
               dp.append(dp[next_num-bit_mark]+1)
           pos += 1

        return dp[0:num+1]

if __name__ == "__main__":
    sol = Solution()
    num = int(sys.argv[1])
    sol.countBits(num)
