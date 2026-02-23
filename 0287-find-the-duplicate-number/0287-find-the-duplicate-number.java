class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0, fast = 0, n = nums.length;
        while(fast!= n){
            slow = nums[slow];
            fast = nums[fast];
            fast = nums[fast]; 
            if (slow == fast ){  //cycle found
                slow = 0;
                while(slow != fast){
                    slow = nums[slow];
                    fast = nums[fast];
                    if(slow == fast){
                         return slow;
                    }
                }
                
            }
        }
        return 0 ;
    }
}