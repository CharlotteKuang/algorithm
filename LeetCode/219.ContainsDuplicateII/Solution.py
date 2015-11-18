ass Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashTable = {}
        
        for i in range(0, len(nums)):
            if not nums[i] in hashTable:
                hashTable[nums[i]] = i
            else:
                pre = hashTable[nums[i]];
                if i - pre <= k: return True
                hashTable[nums[i]] = i
        return False
