# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True
        elif root.left is None and root.right is None: 
            return True
        elif root.left is None or root.right is None:
            return False
        leftNode = root.left
        rightNode = root.right
        return self.helper(leftNode, rightNode)

    def helper(self, leftNode: Optional[TreeNode], rightNode: Optional[TreeNode]) -> bool:
        if leftNode is None and rightNode is None:
            return True
        elif leftNode is None or rightNode is None:
            return False
        if leftNode.val == rightNode.val:
            return self.helper(leftNode.left, rightNode.right) and self.helper(leftNode.right, rightNode.left)
        return False