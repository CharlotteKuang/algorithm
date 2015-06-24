class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0: return 0
            if len(num) == 1: return num[0]
                if len(num) == 2: return max(num[0], num[1])
                amount = [0] * len(num)
                amount[0] = num[0]
                amount[1] = num[1]
                amount[2] = num[0] + num[2]
                result = 0
                for i in range(3, len(num)):
                    amount[i] = max(amount[i-2], amount[i-3]) + num[i]
                        result = max(result, amount[i])
                
            return max(amount[1], amount[2], result)