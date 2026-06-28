class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        res=arr[0]
        nodelete=arr[0]
        onedelete=float('-inf')
        
        for i in range (1,n):
            prev_nodelete = nodelete    #store prev nodelete for curr iteration
            prev_onedelete=onedelete    #store prev onedelete for curr iteration
            nodelete = max(arr[i], prev_nodelete+arr[i])    #can contain either num itself or prevnodelete+num
            if prev_onedelete == float('-inf'): #no number deleted
                v2 = arr[i] #at i=1 only 2 elem we have so if we delete the nums[0] then we have nums[i] only
            else:
                v2 = prev_onedelete + arr[i]
            onedelete = max(v2, prev_nodelete)  #prevnodelete bcz if we delete current elem then prevnodelete is the value
            res = max(res, nodelete, onedelete)

        return res