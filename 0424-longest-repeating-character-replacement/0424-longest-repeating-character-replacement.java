class Solution {
    public int characterReplacement(String s, int k) {
        int low=0, high=0, res=Integer.MIN_VALUE, n=s.length(), diff, mostFreqVal=Integer.MIN_VALUE ; 

        Map<Character, Integer> map = new HashMap<>();

        while(high<n){
            map.put(s.charAt(high), map.getOrDefault(s.charAt(high),0)+1);

            mostFreqVal = Math.max(mostFreqVal, map.get(s.charAt(high)));
            
            diff = (high -low+1) - mostFreqVal ;  /*(currLength-mostfreq apprearing val)
                                                    To count the no of values that need to be modified.*/

            if(diff<=k){    //valid window found.
                res=Math.max(res, high -low+1 );
                high++;      //window expands
            }
            else{   //valid window not found
                while( (high -low+1) - mostFreqVal > k){    //invalid window
                    low++;  //window shrinks.
                    map.put(s.charAt(low-1), map.get(s.charAt(low-1)) - 1 );
                }
                high++;     //window valid so window expand.
            }
        }
        return res;
    }
}