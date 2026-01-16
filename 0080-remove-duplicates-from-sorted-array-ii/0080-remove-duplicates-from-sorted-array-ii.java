//using WHILE loop
class Solution {
    public int removeDuplicates(int[] nums){
        int i = 0 ;
        int j=i;
        int count = 0;
        int n = nums.length;
        while(i<n && j<n){
            if(nums[i] == nums[j]){
                count++;
            }else{
                i++;
                count = 0;
                continue;
            }
            if (count>2){
                for (int k = j ; k<n-1 ; k++){
                    nums[k] = nums[k+1];
                }
                n--;
                j--;
            }
            j++;

        }return n;
    }
}

//using FOR loop
// class Solution {
//     public int removeDuplicates(int[] nums) {
//         int n = nums.length;

//         for (int i = 0; i < n; i++) {
//             int count = 1;

//             for (int j = i + 1; j < n; j++) {
//                 if (nums[i] == nums[j]) {
//                     count++;
//                 } else {
//                     break;
//                 }

//                 if (count > 2) {
//                     for (int k = j; k < n - 1; k++) {
//                         nums[k] = nums[k + 1];
//                     }
//                     n--;   
//                     j--;   
//                 }
//             }
//         }
//         return n;
//     }
// }
