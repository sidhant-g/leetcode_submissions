class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        res=arr[0]
        nodelete=arr[0]
        onedelete=float('-inf') #bestending if one already deleted
        
        for i in range (1,n):
            prev_nodelete = nodelete    #store prev nodelete for curr iteration
            prev_onedelete=onedelete    #store prev onedelete for curr iteration
            nodelete = max(arr[i], prev_nodelete+arr[i])    #can contain either num itself or prevnodelete+num
            if prev_onedelete == float('-inf'): #no number deleted
                v2 = arr[i] #if nothing deleted then only we can keep arr[i] in onedelete 
                            #v2=arr[i] means we are starting at arr[i]
            else:
                v2 = prev_onedelete + arr[i]
            onedelete = max(v2, prev_nodelete)  #prevnodelete bcz if we delete current elem then prevnodelete is the value
            res = max(res, nodelete, onedelete)

        return res