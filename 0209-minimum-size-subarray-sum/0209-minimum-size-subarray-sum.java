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
                high=i;         //first window found...
            }
            if(sum>=target){
                len= Math.min(len, high-low+1);     //length of 1st sliding window stored...
                while(high<n && low<n){                    
                    low++;
                    if(low==n){
                        return len;        
                    }
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
        return 0 ;        
    }
}