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
        if p.val > q.val:
            self.helper(node, q, p)
        else:
            self.helper(node, p, q)        
        return self.ans

    def helper(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
        if node == None:
            return 0
        elif node == p or node == q:    #we found one of the node that we wanted so other would obv be below it, so we got LCA
            self.ans = node
            return 0
        elif node.val < p.val:
            self.helper(node.right, p, q)       
        elif node.val > q.val:
            self.helper(node.left, p, q)
        else:
            self.ans = node
            return 0