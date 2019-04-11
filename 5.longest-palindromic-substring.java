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
    public String longestPalindrome(String s) {
        if(s.length()==1) return s;
        String longest = "", curr = "";
        for(int i = 0; i < s.length() - 1; i++){
            if(s.substring(i, i+1).equals(s.substring(i + 1, i+2))){
                curr = s.substring(i, i+1) + s.substring(i, i+1);
                System.out.println("currDouble: " + curr + i);
                for(int j = 1; j < Math.min(i - 0, s.length() - i - 1) + 1; i++) {
                    if(s.substring(i-j, i-j+1).equals(s.substring(i+j+1, i+j+2))) 
                       curr = s.substring(i-j, i-j+1) + curr + s.substring(i-j, i-j+1);
                     else break;
                }
            } else if(i > 0 && i < s.length() - 1 && s.substring(i-1, i).equals(s.substring(i+1, i+2))){
                curr = s.substring(i, i+1);
                System.out.println("currSingle: " + curr + i);
                for(int j = 1; j < Math.min(i - 0, s.length() - i) + 1; j++) {
                    System.out.println("currfront: " + s.substring(i-j, i-j+1) + " currback: " + s.substring(i+j, i+j+1) + "j: " +j + i);
                    if(s.substring(i-j, i-j+1).equals(s.substring(i+j, i+j+1))) {
                        curr = s.substring(i-j, i-j+1) + curr + s.substring(i-j, i-j+1);
                        System.out.println("currCombine: " + curr + i);
                    }
                    else break;
                }
            } else{
                curr = s.substring(i, i+1);
            }
            if (curr.length() > longest.length()) {
                longest = curr;
            }
        }
        return longest;   
    }
}
