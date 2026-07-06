class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n=len(nums1)
        m=len(nums2)
        for i in range(0, n):
            j=0
            while j<m and nums2[j] != nums1[i]:
                j+=1
            # if j == m here it means no elem in nums2 is equal to nums1[i]
            k=j
            j=k+1
            while j<m:  
                if nums2[j]>nums2[k] :
                    ans.append(nums2[j])         
                    break
                j+=1
            if j==m:
                ans.append(-1)
        return ans