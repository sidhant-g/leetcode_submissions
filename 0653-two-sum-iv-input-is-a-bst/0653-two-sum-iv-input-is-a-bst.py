# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node = root
        asc = []    #stack to store min elem 
        desc = []   #stack to store max elem 
        if node == None:
            return False
        while node:     #keep storing in min stack while next left node is  not null
            asc.append(node)
            node = node.left
        node = root     # again start from root for making desc 
        while node:     #keep sotring in max stack while next right node is not null
            desc.append(node)
            node = node.right
        i = self.getSmall(asc)
        j = self.getBig(desc)

        while ((i and j) and (i!=j) and (i.val <= j.val)):  #i & j are not null & they are different nodes & i.val<=j.val
            sum = i.val + j.val
            if sum == k:
                return True
            elif sum < k:
                i = self.getSmall(asc)  #the smallest was popped now it will give the next slightly bigger number.
            else:   #sum>k
                j = self.getBig(desc)
        return False

    def getSmall(self, asc: list[int]) -> Optional[TreeNode]:   # gets the smallest number each time 
        if not asc:
            return None
        small = asc[-1]     #smallest num on top of min stack
        asc.pop()
        #as smallest is on the leftmost node so now no more left nodes exist so call the right node from here 
        rightChild = small.right
        #then continue left node iterations again for the right node
        while rightChild:
            asc.append(rightChild)
            rightChild = rightChild.left
        return small

    def getBig(self, desc: list[int]) -> Optional[TreeNode]:
        if not desc:
            return None
        big = desc[-1]
        desc.pop()
        leftChild = big.left
        while leftChild:
            desc.append(leftChild)
            leftChild = leftChild.right
        return big