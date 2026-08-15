# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        curr_level = 0
        res = []
        if root == None:
            return []
        while queue:
            level_size = len(queue)
            tmp = []
            curr_level += 1
            while level_size:
                t = queue [0]
                queue.popleft()
                tmp.append(t.val)
                if t.left != None:
                    queue.append(t.left)
                if t.right != None:
                    queue.append(t.right)
                level_size -=1
            if curr_level %2 == 0:  #even level 
                tmp.reverse()
                res.append(tmp)
            else:                   #odd level
                res.append(tmp)
        return res                    