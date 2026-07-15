class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n -1 
        while low<=high:
            mid  = (low+high) // 2
            if mid == 0 :    #edge case - peak at start of arr
                if n == 1 or arr[0] > arr[1]:   # if single elem array or 0th elem is the peak
                    return 0
                low = 1 #if peak not at 0th index then keep low = 1 to check arr[mid-1] further as arr[-1] would give error
                continue
            elif mid == n - 1 :  #edge case - peak at end of arr
                if arr[n-1] > arr[n-2]: # last elem is the peak elem
                    return n-1
                high = n-2  # if the last elem not peak but still if mid=n-1 then do high=n-2 as arr[mid+1] at mid=n-1 give error
                continue
            #no boundary conditions
            else:    
                if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]: #peak found
                    return mid
                elif arr[mid] < arr[mid+1] and arr[mid] > arr[mid-1] :   #peak elem further in arr
                    low = mid+1
                else:  # arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]   peak elem left behind in the array
                    high = mid-1