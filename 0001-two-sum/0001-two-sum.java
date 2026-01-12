// class Solution {
//     public int[] twoSum(int[] nums, int target) {
//         Arrays.sort(nums);
//         int start  = 0; 
//         int end  = nums.length-1;
//         int sum = 0;
//         while(start < end ){
//             sum = nums[start]+nums[end];
//             if (sum == target){
//                 return new int[] {start , end };
//             }
//             else if (sum < target){
//                 start ++;
//             }
//             else{
//                 end--;
//             }
//         }return new int[] {0};
//     }
    
// }
import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        int n = nums.length;
        int[][] arr = new int[n][2];

        // store value and original index
        for (int i = 0; i < n; i++) {
            arr[i][0] = nums[i];
            arr[i][1] = i;
        }

        // sort by value
        Arrays.sort(arr, (a, b) -> a[0] - b[0]);

        int start = 0;
        int end = n - 1;

        // one loop + two pointers
        while (start < end) {
            int sum = arr[start][0] + arr[end][0];

            if (sum == target) {
                return new int[] { arr[start][1], arr[end][1] };
            } 
            else if (sum < target) {
                start++;
            } 
            else {
                end--;
            }
        }

        return new int[] {};
    }
}
