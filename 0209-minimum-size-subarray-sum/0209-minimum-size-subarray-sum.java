class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int len = Integer.MAX_VALUE;
        int low=0;
        int high=low;
        int sum=0;

        while(high<n){
            sum+= nums[high];               //keep hiring till kaam na hoye
            while(sum>=target){
                len = Math.min(len, high-low+1);    //update smallest len
                low++;
                sum-= nums[low-1];           //keep firing if kaam horha
            }
            high++;                         //again hire if kaam nii hora
        }  
        if(len==Integer.MAX_VALUE){
            return 0;                       //NO sum>=target found
        }
        else{
            return len;
        }
    }
}