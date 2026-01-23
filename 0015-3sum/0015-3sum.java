//TLE soln at end...
//OPTIMAL
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        int n = nums.length;
        int s ;

        Arrays.sort(nums);

        List<List<Integer>> result = new ArrayList<>();
        
        for (int i=0 ; i<n-2 ;i++){
            if (i>0 && nums[i]== nums[i-1]){
                continue;
            }
            int l=i+1;
            int r=n-1;
            while(l<r){
                s = nums[i]+nums[l]+nums[r];  //OR sum==nums[l]+nums[r]
                if (s == 0){                  //and check acc to sum== -nums[i]
                    result.add(Arrays.asList(nums[i] , nums[l] , nums[r]));
                    l++;
                    r--;
                    while(l<r && nums[l]==nums[l-1]){  //or l<n
                        l++;
                    }
                    while(r>l && nums[r] == nums[r+1] ){  //or r>0
                        r--;
                    }
                }
                else if (s>0){
                    r--;
                }
                else{
                    l++;
                }
            }
        }return result;
    }
}

//TLE error...
// class Solution {
//     public List<List<Integer>> threeSum(int[] nums) {
//         int n = nums.length;

//         Arrays.sort(nums);

//         List<List<Integer>> result = new ArrayList<>();

//         for (int i = 0; i < n - 2; i++) {
//             if (i> 0 && nums[i] == nums[i-1]){
//                 continue ;
//             }
//             for (int j = i + 1; j < n - 1; j++) {
//                 if (j>i+1 && nums[j]==nums[j-1]){
//                     continue ;
//                 }
//                 for (int k = j + 1; k < n; k++) {
//                     if(k>j+1 && nums[k] == nums[k-1]){
//                         continue;
//                     }
//                     if (nums[i] + nums[j] + nums[k] == 0) {
//                         List<Integer> triplet = new ArrayList<>();
//                         triplet.add(nums[i]);
//                         triplet.add(nums[j]);
//                         triplet.add(nums[k]);
//                         result.add(triplet);
                        
//                     } else {
//                         continue;
//                     }
//                 }
//             }
//         }
//         return result;
//     }
// }