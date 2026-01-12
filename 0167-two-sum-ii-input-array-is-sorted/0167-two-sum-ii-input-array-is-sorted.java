 //BRUTE SOLN...

// class Solution{
//     public static int[] twoSum(int[] numbers , int target){
//         for (int i = 0 ; i< numbers.length ; i++){
//             for (int j = i+1 ; j<numbers.length ; j++){
//                 if (numbers[i]+numbers[j] == target){
//                     return new int[] {i+1 , j+1};
//                 }
        
//             }                //BRUTE SOLN...
//         }
//         return new int[] {0} ;
//     }
// }

//BETTER SOLN...

// class Solution{
//     public int[] twoSum(int[] numbers , int target){
//         HashMap<Integer ,Integer>map = new HashMap<>();
//         for (int i=0 ; i<numbers.length; i++){
//             map.put(numbers[i],i);
//         }
//         for (Map.Entry<Integer ,Integer > e1 : map.entrySet()){
//             for (Map.Entry<Integer , Integer> e2 : map.entrySet()){
//                 if(!e1.getKey().equals(e2.getKey())){
//                     int sum = e1.getKey()+e2.getKey();
//                     if(sum == target){
//                         return new int[] {e1.getValue()+1 , e2.getValue()+1};
//                     }
//                 }
//             }
//         }
//         return new int[] {0};
//     }
// }

//OPTIMAL SOLN...

class Solution {
    public int[] twoSum(int[] numbers , int target){
        int start = 0 ; 
        int end = numbers.length-1;
        while(start<end){
            if(numbers[start]+numbers[end]== target){
                return new int[] {start+1 , end+1};
             }

            else if (numbers[start]+numbers[end]<target){
                start++;            
            }
            else{
                end--;
            } 
        }
        return new int[] {0};
    }
        
}