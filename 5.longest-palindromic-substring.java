/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 *
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (26.88%)
 * Total Accepted:    518.5K
 * Total Submissions: 1.9M
 * Testcase Example:  '"babad"'
 *
 * Given a string s, find the longest palindromic substring in s. You may
 * assume that the maximum length of s is 1000.
 * 
 * Example 1:
 * 
 * 
 * Input: "babad"
 * Output: "bab"
 * Note: "aba" is also a valid answer.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "cbbd"
 * Output: "bb"
 * 
 * 
 */
class Solution {
    public String longestPalindromeOrigianl(String s) {
        if(s.length()<=1 || s == null) return s;
        String longest = "", curr = "", curr2="";
        for(int i = 0; i < s.length() - 1; i++){
            if(s.charAt(i) == s.charAt(i + 1)){
                curr = s.substring(i, i+2);
                for(int j = 1; j < Math.min(i+1, s.length() - i - 1); j++) {
                    if(s.charAt(i-j) == s.charAt(i+j+1)) {
                        curr = s.substring(i-j, i+j+2);
                    } else break;
                }
            } 
            if(i > 0 && i < s.length() - 1 && s.charAt(i-1) == s.charAt(i+1)){
                curr2 = s.substring(i, i+1);
                for(int j = 1; j < Math.min(i + 1, s.length() - i); j++) {
                    if(s.charAt(i-j) == s.charAt(i+j)) {
                        curr2 = s.substring(i-j, i+j+1);
                    }
                    else break;
                }
            } else{
                curr2 = s.substring(i, i+1);
            }
            curr = curr.length() > curr2.length() ? curr : curr2;
            if (curr.length() > longest.length()) {
                longest = curr;
            }
        }
        return longest;   
    }
    // optimization: 
    // 1. Instead of updating the curr/curr2 string, update two index will be easier, using substring at the end
    // 2. generalize: find the similarities/generalizations of cases; integrate them
    // 3. give a generalized constraints for array such as i >= 0 && i < s.length, don't care about the specific details for different cases.
    public String longestPalindrome(String s) {
        if(s == null || s.length() < 1) return "";
        int len1 = 0, len2 = 0, start = 0, end = 0, len = 0;
        for(int i = 0; i < s.length(); i++) {
            len1 = FindPalidrome(s, i, i);
            len2 = FindPalidrome(s, i, i+1);
            len = Math.max(len1, len2);
            if(len > end - start) {
                start = i - (len-1) / 2;
                end = i + len/2 + 1;
            }
        }
        return s.substring(start, end);
    }
    
    public int FindPalidrome(String s, int left, int right) {
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }
        return right - left - 1;
    }
    
    public String longestPalindromeDP(String s) {
        boolean [][] dp = new boolean[s.length()][s.length()];
        String res = "";
        for(int i = s.length() - 1; i >= 0; i--){
            for(int j = i; j < s.length(); j++) {
                dp[i][j] = (s.charAt(i) == s.charAt(j)) && (j - i < 2 || dp[i+1][j-1]);
                if(dp[i][j] && j - i + 1> res.length())
                    res = s.substring(i, j+1);
            }
        }
        return res;
    }
    // DP solution: 
    // 1. Think recurisively, if a larger/longer requirement to be meet, it's component must meet the requirement
    // 2. tricky: set up the nested for loop, outerloop back to front, inner loop from i to back
}