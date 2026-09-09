# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       currsum = 0
       node = root
       self.helper(node, currsum)
       return self.res

    def helper(self, node: Optional[TreeNode], currsum: int) -> int:
        if node == None:
            return 0
        left = self.helper(node.left, currsum)
        right = self.helper(node.right, currsum)
        currsum = left+right
        self.res = max(self.res, currsum)
        return 1+max(left, right)