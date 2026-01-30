class Solution {
    public int totalFruit(int[] fruits) {
        int low=0,high=0, n=fruits.length , maxLen = 0; 
        Map<Integer, Integer> map = new HashMap<>();

        while(high<n){
            map.put(fruits[high] , map.getOrDefault(fruits[high],0)+1);

            if(map.size()<=2){
                maxLen = Math.max(maxLen , high-low+1);
            }
            else{
                while(map.size()>2){
                    map.put(fruits[low] , map.get(fruits[low])-1);
                    if(map.get(fruits[low])==0){
                        map.remove(fruits[low]);
                    }
                    low++;
                }
            }
            high++;
        }
        return maxLen ; 
    }
}