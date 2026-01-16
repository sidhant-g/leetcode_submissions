class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int j =0;
        int total = m+n;
        while (j<n){
            nums1[m]=nums2[j];
            m++;
            j++;            
        }
        int temp;
        int i  =0 ;

        while(i<total-1){
             if(nums1[i]>nums1[i+1]){
                temp = nums1[i+1];
                nums1[i+1] = nums1[i];
                nums1[i] = temp;
                i =0;
                continue;
             }i++;
        }
    }
}