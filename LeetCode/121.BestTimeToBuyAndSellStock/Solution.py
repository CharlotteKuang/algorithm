class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        
        dp = [0]# for i in range(len(prices))]
        rst = 0
        for i in range(1, len(prices)):
            #if prices[i] - prices[i-1] + dp[i-1] > dp[i]:
            dp.append(max(prices[i]-prices[i-1]+dp[i-1], 0))
            rst = max(rst, dp[i])
        return rst
