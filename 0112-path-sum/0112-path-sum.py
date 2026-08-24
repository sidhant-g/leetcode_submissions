# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        node = root
        currSum = 0
        return self.helper(node, targetSum, currSum)

    def helper(self, node: Optional[TreeNode], targetSum: int, currSum: int) -> bool:
        if not node:
            return False
        currSum += node.val
        if not node.left and not node.right:
            return currSum == targetSum 
        left = self.helper(node.left, targetSum, currSum) 
        right = self.helper(node.right, targetSum, currSum)       
    
        return left or right