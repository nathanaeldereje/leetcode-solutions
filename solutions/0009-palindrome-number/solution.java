class Solution {
     public static boolean isPalindrome(int x) {
        String z=Integer.toString(x);
        int check=0;
        int j=z.length()-1;
        for(int i=0;i<=(z.length())/2;i++){

            if(z.charAt(i)!=z.charAt(j)) {
                check=-1;
                return false;

            }
            j--;
        }
        return true;
    }
    
}

