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
        res = []
        leftToRight = 1 #root insertion starts from left to right
        if root == None:
            return []
        while queue:
            level_size = len(queue)
            tmp = [None] * level_size
            #size of tmp or total nodes in this level
            first = 0
            last = level_size - 1
            while level_size:
                t = queue [0]
                queue.popleft()
                if leftToRight :
                    tmp[first] = t.val
                    first+=1
                else:               #insert righttoLeft for this level
                    tmp[last] = t.val   #the leftmost node is inserted at rightmost position
                    last-=1
                if t.left != None:
                    queue.append(t.left)
                if t.right != None:
                    queue.append(t.right)
                level_size -=1
            res.append(tmp)
            leftToRight = not leftToRight
        return res                    