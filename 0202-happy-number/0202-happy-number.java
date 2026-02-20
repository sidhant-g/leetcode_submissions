class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set = new HashSet<>();
        int store;
        set.add(n);

        if (n == 1){
            return true ;
        }

        while(!set.contains(sumOfSquares(n))){
            store = sumOfSquares(n) ;
            set.add(store);
            if (store == 1){
                return true;
            }
            n = store ; 
        }
        return false ;  
    }
    public int sumOfSquares( int n ){
        int sum = 0;
        while (n!=0){
            int temp = n ;
            temp = temp%10;
            sum = sum+temp*temp ;
            n = n/10 ; 
        }
        return sum ;
    }
}