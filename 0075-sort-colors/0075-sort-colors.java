class Solution {
    public void sortColors(int[] nums) {
        int n =nums.length;
        int low = 0, mid =0, high=n-1;

        while(mid<=high){
            if(nums[mid]==0){
                swap(nums, mid, low);
                low++;
                mid++;
            }
            else if(nums[mid]==1){
                mid++;
            }
            else{       //mid==2
                swap(nums, high, mid);
                high--;
            }
        }
    }    
    private void swap(int[] nums , int small, int big){
        int temp = nums[small];
        nums[small] = nums[big];
        nums[big] = temp;
    }
}



//  if (n==0 || n==1){
//             return;
//         } 
//         for(int i = 0 ; i<n-1 ; i++){
//             for(int j = 0 ; j<n-1-i ;j++){
//                 if (nums[j]>nums[j+1]){
//                     temp = nums[j+1];
//                     nums[j+1]=nums[j];
//                     nums[j]=temp;
//                 }
//             }
//         }