class Solution {
    public boolean validPalindrome(String s) {
        return helper(s, 0, s.length()-1, false);
    }
    private boolean helper(String s, int l, int r, boolean removed){
        if(l>=r)
            return true;
        if(s.charAt(l)!=s.charAt(r))
            if(removed)
                return false;
            else
                return helper(s, l+1, r, true) || helper(s, l, r-1, true);
        else
            return helper(s, l+1, r-1, removed);
    }
}
