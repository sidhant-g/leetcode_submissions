# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        node = root
        self.helper(node, p, q)
        return self.ans

    def helper(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int :
        if node == None:
            return 0
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)
        own = 0
        if (node == p or node == q ):
            own = 1
        total = left+right+own
        if total == 2 and self.ans == None:
            self.ans = node
        return total