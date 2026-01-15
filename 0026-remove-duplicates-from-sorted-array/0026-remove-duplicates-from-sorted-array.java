class Solution{
    public int removeDuplicates(int[] nums){
         int i =0;
         int j = i+1;
         int unique = 1;
         while(i<nums.length-1 && j<nums.length){
            if(nums[j] != nums [j-1]){
                nums[i+1]=nums[j];
                i++;
                j++;
                unique++;
                continue;
            }
            j++;    //i placed at unique elem & only increases when unique elem found.
        }
        return unique;
    }
    
}