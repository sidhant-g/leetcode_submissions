class Solution {
    public int longestOnes(int[] nums, int k) {
        int low=0, high=0, res=0, n =nums.length, count=0, zeroes ;

        while(high<n){

            if(nums[high]==1){
                count++;        //keep the count of 1.
            }

            zeroes = (high-low+1) - count ;     //number of elements that need to be modified.

            if(zeroes<=k){     //valid window (The elements that need to be modifed can be modified)
                res = Math.max(res, (high-low+1)); 
                high++;     //window expands
            }
            else{         
                while((high-low+1) - count > k){  //invalid window( elements that need to be modified can't be modiified)
                    low++;
                    if(nums[low-1]==1){
                        count--;    
                    }
                }
                high++;     //now valid window So, window expand
            }
        }
        return res;
    }
}