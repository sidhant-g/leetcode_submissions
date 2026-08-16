# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        firstNode = p
        secondNode = q
        return self.helper(firstNode, secondNode)
    
    def helper(self, firstNode: Optional[TreeNode], secondNode: Optional[TreeNode]) -> bool:
        #both nodes null, they identical
        if firstNode is None and secondNode is None:
            return True 
        #if both not null, then, one of them can be null or either both can contain values
        elif firstNode is None or secondNode is None:
            return False
        #if both nodes contain values
        if firstNode.val == secondNode.val :
            return self.isSameTree(firstNode.left, secondNode.left) and self.isSameTree(firstNode.right, secondNode.right)
        #if currNodes have different val, then not identical
        return False