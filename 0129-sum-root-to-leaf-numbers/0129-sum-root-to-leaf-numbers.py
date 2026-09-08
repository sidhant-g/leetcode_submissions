# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        currSum = 0 
        res = 0
        node = root
        self.helper(node, currSum, res)
        return self.res

    def helper (self, node: Optional[TreeNode],  currSum: int, res: list[int]) -> None:
        if node is None : 
            return 

        currSum  = (currSum*10)+node.val

        if node.left == None and node.right == None:
            self.res+=currSum
            return 
        
        self.helper(node.left, currSum, res)
        self.helper(node.right, currSum, res)
        return