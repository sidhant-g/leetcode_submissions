# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    currSum = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.currSum = 0
        path = 0 
        node = root
        self.helper(node, path)
        return self.currSum

    def helper(self, node: Optional[TreeNode], path: str) -> None:
        if not node:
            return
        path = path * 10 + node.val
        if (not node.left) and (not node.right):
            self.currSum += path

        self.helper(node.left, path)
        self.helper(node.right, path)
        path = path - (path % 10)