class Solution {
    public String minWindow(String s, String t) {
        int low = 0, high =0, m = s.length(), n= t.length() , res=Integer.MAX_VALUE, start=0, end=0;
        
        Map<Character, Integer> have = new HashMap<>();
        Map<Character, Integer> need = new HashMap<>();

        for(char ch : t.toCharArray()){
            need.put(ch, need.getOrDefault(ch, 0)+1);            
        }

        while(high< m ){
            have.put(s.charAt(high), have.getOrDefault(s.charAt(high), 0)+1);
            while(correctSubStr(have, need)){
                if(res > high-low+1){
                    res = high-low+1;
                    start = low;
                    end = high;
                }
                
                low++;
                have.put(s.charAt(low-1), have.get(s.charAt(low-1))-1);
                if(have.get(s.charAt(low-1))==0){
                    have.remove(s.charAt(low-1));
                }
            }
            high++;
        }

        
        if(res==Integer.MAX_VALUE){
            return "";
        }
        else{
            return s.substring(start, end+1);
        }
    }
    boolean correctSubStr(Map<Character, Integer> have, Map<Character, Integer> need){
        for(char c : need.keySet()){
            if(have.getOrDefault(c, 0) < need.get(c)){
                return false; 
            }
        }           
        return true;    //assume valid SubStr
    }
}