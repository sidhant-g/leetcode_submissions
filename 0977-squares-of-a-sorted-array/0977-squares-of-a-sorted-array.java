// optimal
class Solution {
    public int[] sortedSquares(int[] nums) {
        int j = 0;
        int i = 0;
        int n = nums.length;
        List<Integer> nega = new ArrayList<>();
        List<Integer> posi = new ArrayList<>();
        List<Integer> result = new ArrayList<>();
        
        while (i < n) {   // fixed loop condition
            if (nums[i] < 0) {
                nega.add(nums[i] * nums[i]);
            } else {
                posi.add(nums[i] * nums[i]);
            }
            i++;
        }
        
        i = 0;
        Collections.reverse(nega);
        
        while (i < nega.size() && j < posi.size()) {
            if (nega.get(i) < posi.get(j)) {
                result.add(nega.get(i));
                i++;
            } else {
                result.add(posi.get(j));
                j++;
            }
        }     
        
        while (j < posi.size()) {
            result.add(posi.get(j));
            j++;
        }
        
        while (i < nega.size()) {
            result.add(nega.get(i));
            i++;
        }
        
        // convert List<Integer> to int[]
        int[] resArray = result.stream().mapToInt(Integer::intValue).toArray();
        return resArray;
    }
}
