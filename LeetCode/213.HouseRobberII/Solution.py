class Solution:
    def robLine(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        money = [nums[0], nums[1], nums[0]+nums[2]]
        result = max(money)
        for i in range(3, len(nums)):
            money.append(max(money[i-2], money[i-3]) + nums[i])
            result = max(money[-1], result)
        return result
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums:
            if 0 < len(nums) <= 3: return max(nums)
            else: return max(self.robLine(nums[0:len(nums)-1]), self.robLine(nums[1:len(nums)]))
        else: return 0