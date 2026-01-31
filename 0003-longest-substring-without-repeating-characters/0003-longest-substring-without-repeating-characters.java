class Solution {
    public int lengthOfLongestSubstring(String s) {
        int low=0, high=0, n=s.length(), len=0;

        Map<Character, Integer> map = new HashMap<>();

        while(high<n){
            map.put(s.charAt(high), map.getOrDefault(s.charAt(high), 0)+1);
            if(map.get(s.charAt(high))==1){
                len = Math.max(len, high-low+1);
                high++;
            }
            else{
                while(map.get(s.charAt(high))!=1){
                    map.put(s.charAt(low), map.get(s.charAt(low))-1);
                    if(map.get(s.charAt(low))==0){
                        map.remove(s.charAt(low));
                    }
                    low++;
                }
                high++;
            }
        }
        if(len!=0){
            return len;
        }
        else{
            return 0;
        }

    }
}