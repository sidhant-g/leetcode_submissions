class Solution {
    public int[] twoSum(int[] nums , int target){
         int n = nums.length;
         int[][] arr = new int[n][2];
        for (int i = 0 ; i<nums.length ; i++){
            arr[i][0] = nums[i];
            arr[i][1] = i ;  
        }
        //Sort the function
        Arrays.sort(arr , (a , b ) -> a[0] - b[0]);


        int start = 0;
        int end = nums.length-1;
        int sum ;
        while (start<end){
            sum = arr[start][0]+arr[end][0];
            if (sum == target ){
                return new int[] {arr[start][1] , arr[end][1]};
            }
            else if (sum < target ){
                start++;
            }
            else{
                end--;
            }
        }
        return new int[] {0} ; 
    }
}