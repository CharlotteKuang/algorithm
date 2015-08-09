# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBSTHelper(self, nums, head, tail):
        if head > tail: return None
        mid = (head+tail)/2
        root = TreeNode(nums[mid])
        root.left, root.right = self.sortedArrayToBSTHelper(nums, head, mid-1), self.sortedArrayToBSTHelper(nums, mid+1, tail)
        return root
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        return self.sortedArrayToBSTHelper(nums, 0, len(nums)-1)
        
