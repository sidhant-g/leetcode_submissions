# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    galat = 0
    galat1_left = None
    galat1_right= None
    galat2_left = None
    galat2_right = None
    prev = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        node = root
        self.helper(node)
        temp = None
        if self.galat == 1:
            temp = self.galat1_right.val
            self.galat1_right.val = self.galat1_left.val
            self.galat1_left.val = temp
        else:       #more than 1 nodes are wrong
            temp = self.galat2_right.val
            self.galat2_right.val = self.galat1_left.val
            self.galat1_left.val = temp

    def helper(self, node: Optional[TreeNode]) -> None:
        if node == None :
            return None
        self.helper(node.left)
        if self.prev == None:
            self.prev = node
        else: 
            if node.val < self.prev.val: #galat found
                if self.galat == 0: #no galat node found before
                    self.galat1_left  = self.prev
                    self.galat1_right= node
                    self.galat+=1
                else:               #galat node found before
                    self.galat2_left = self.prev 
                    self.galat2_right= node
                    self.galat+=1
        self.prev = node
        self.helper(node.right)
