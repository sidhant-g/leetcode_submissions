class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] sqNums  = new int[n];
        for (int i =0 ; i<n ; i++){
            sqNums[i] = nums[i]*nums[i];
        }
        Arrays.sort(sqNums);
        return sqNums;

    }
}