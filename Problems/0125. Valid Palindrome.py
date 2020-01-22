class Solution {
    public boolean isPalindrome(String s) {
        if(s.isEmpty())
            return true;
        s = s.toLowerCase();
        s = s.replaceAll("[^a-z0-9]", "");
        int i=0, j=s.length()-1;
        while(i<j)
            if(s.charAt(i++)!=s.charAt(j--))
                return false;
        return true;
    }
}
