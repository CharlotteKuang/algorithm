import sys
import pdb

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #pdb.set_trace() 
        dp = [0]*(amount+1)

        for i in range(1, amount+1):
            min_coin = sys.maxint
            for coin in coins:
                if coin <= i: 
                    min_coin = min(dp[i-coin]+1, min_coin) 
            dp[i] = min_coin
        if dp[amount] == sys.maxint:
            return -1
        else:
            return dp[amount]

if __name__ == "__main__":
    cases = [([1, 2, 5], 11), ([2], 3)]
    sol = Solution()

    for case in cases:
        print sol.coinChange(case[0], case[1])
