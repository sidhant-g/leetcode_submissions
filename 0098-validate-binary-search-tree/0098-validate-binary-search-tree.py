# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = True
    prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node = root
        res = []
        self.helper(node, res)
        return self.ans

    def helper(self, node: Optional[TreeNode], res: list[int]) -> None:
        if node == None:
            return None
        self.helper(node.left, res)
        if self.prev == None:
            self.prev = node
        else:
            if node.val <= self.prev.val:
                self.ans = False
            self.prev = node
        res.append(node.val)
        self.helper(node.right, res)