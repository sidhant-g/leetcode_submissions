class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;
        int s = nums[0] ;
        int max = -1000000;    //check max when sum<target     ->BOTH Max & Min 
        int min = 1000000;    //check min when sum>target        for 1st iteration & storing only...

        Arrays.sort(nums);

        for (int i=0 ; i<n-2 ;i++){
            if (i>0 && nums[i]== nums[i-1]){
                continue;
            }
            int l=i+1;
            int r=n-1;
            while(l<r){
                s = nums[i]+nums[l]+nums[r];
                if(s == target){
                    return s;
                }
                else if(s<target){
                    max = Math.max(max , s);
                    l++;
                }
                else {          // s > target
                    min = Math.min(min , s);
                    r--;
                }

            }
        }
        int diff1 = target - max ;
        int diff2 = min -target;
        if(diff1 == diff2 ){
            return max;     //OR min (same same)
        }
        else if (diff1<diff2 || diff1 == target){    //max closer to target
            return max;
        }
        else {          //diff2<diff1 diff2==target
            return min;            //min is closer to target
        }
    }
}