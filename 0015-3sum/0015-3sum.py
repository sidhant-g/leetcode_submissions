class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        i = 0
        res_list = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i+1
            k = n - 1
            while j < k:            #Calc 2Sum for each i
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum < 0:
                    j += 1
                    continue
                elif curr_sum > 0:
                    k -= 1
                    continue
                else:
                    res_list.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        return res_list
