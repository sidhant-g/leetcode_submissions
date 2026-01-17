class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int idx = m + n - 1;
        while (i>=0 && j>=0) {
            if (nums1[i] > nums2[j]) {
                nums1[idx] = nums1[i];
                i--;
                idx--;
            } else {
                nums1[idx] = nums2[j];
                j--;
                idx--;
            }

        }
        while (j>=0){            //elem finish in nums1. put elem of j in nums1
            nums1[idx] = nums2[j];
            j--;
            idx--;
        }
        while(i>=0){            //elem finish in nums2. put elem of nums1 in nums1
            nums1[idx] = nums1[i];
            i--;
            idx--;
        }
    }
}

//         int i=0;
//         int total = m+n;
//         while (i<n){
//             nums1[m]=nums2[i];
//             m++;
//             i++;            
//         }
//         int temp;
//         i  =0 ;

//         while(i<total-1){
//              if(nums1[i]>nums1[i+1]){
//                 temp = nums1[i+1];
//                 nums1[i+1] = nums1[i];
//                 nums1[i] = temp;
//                 i =0;
//                 continue;
//              }i++;
//         }
//     }
// }