class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length()-1;
        while (left<right) {
            
            if (s.charAt(left) != s.charAt(right)) { 
                return (isProperPalindrome(s.substring(left+1, right+1)) || 
                        isProperPalindrome(s.substring(left, right)));
            }
            
            left++;
            right--;
        }
        return true;
    }
    
    private boolean isProperPalindrome(String s) {
        int length = s.length();
        if (length==0) { 
            return false; 
        }
        for (int i=0; i<length/2; i++) {
            if (s.charAt(i)!=s.charAt(length-i-1)) { 
                return false; 
            }
        }
        return true;
    }
}
