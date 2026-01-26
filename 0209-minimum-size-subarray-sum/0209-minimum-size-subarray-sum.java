class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int len = Integer.MAX_VALUE;
        int low=0;
        int high=low;
        int sum=0;

        for(int i=low;  i<n; i++){
            sum += nums[i];
            if(sum<target){
                continue;
            }
            else{
                high=i;
            }
            if(sum>=target){
                while(high<n && low<n){
                    len= Math.min(len, high-low+1);
                    low++;
                    sum = sum -nums[low-1];
                    if(sum>=target){
                        len=Math.min(len, high-low+1);
                    }
                    else{
                        high++;
                        if(high==n){
                            return len;
                            
                        }
                        sum+=nums[high];
                        len = Math.min(len,high-low+1);
                    }
                } 
            }
            
        }
        if(len==Integer.MAX_VALUE){
            return 0 ;
        }
        else{
            return len;
        }
    }
}