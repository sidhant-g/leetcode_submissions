# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []
        if root == None:
            return []
        while queue:
            level_size = len(queue)
            tmp = []
            while level_size:
                t = queue[0]
                queue.popleft()
                tmp.append(t.val)
                if t.left != None:
                    queue.append(t.left)
                if t.right != None:
                    queue.append(t.right)
                level_size -= 1
            res.append(tmp)
        return res