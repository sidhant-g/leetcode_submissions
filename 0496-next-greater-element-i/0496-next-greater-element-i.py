class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        res = [-1] * m
        j=0
        stack = []
        mp = defaultdict(int)
        for i in range (0,m):   #maps elem of nums1 to their index
            mp[nums1[i]] = i  
        while j < n:
            # only insert in stack if the nums2[j] is present in nums1 and other considions
            if  nums2[j] in mp and (not stack or nums2[j]<= stack[-1]) : 
                stack.append(nums2[j])
            else:   # nums2[j] not in nums1 or nums2[j] > stack.(top)
                while stack and nums2[j] > stack[-1]:
                    index = mp[stack[-1]]
                    res[index] = nums2[j]
                    stack.pop()
                if nums2[j] in mp:  #if the greater elem found is present in map then append
                    stack.append(nums2[j])
            j+=1
        return res