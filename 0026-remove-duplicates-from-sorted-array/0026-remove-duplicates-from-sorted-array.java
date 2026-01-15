class Solution{
    public int removeDuplicates(int[] nums){
        int i =0 ;
        int j =1 ;
        int uniq = 1;
        int n = nums.length;
        while(i<n-1 && j<n){
            if (nums[j]!=nums[j-1]){
                nums[i+1] = nums[j];
                i++;     // i only increase when unique elem found
                uniq++;
            }
            j++;     //j increases in every condition
        }  
        return uniq;      
    }
}















// class Solution{
//     public int removeDuplicates(int[] nums){
//          int i =0;
//          int j = i+1;
//          int unique = 1;
//          while(i<nums.length-1 && j<nums.length){
//             if(nums[j] != nums [j-1]){
//                 nums[i+1]=nums[j];
//                 i++;
//                 j++;
//                 unique++;
//                 continue;
//             }
//             j++;    //i placed at unique elem & only increases when unique elem found.
//         }
//         return unique;
//     }
    
// }