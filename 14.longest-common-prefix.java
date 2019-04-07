import java.util.HashMap;

/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (33.19%)
 * Total Accepted:    435.4K
 * Total Submissions: 1.3M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 * Example 1:
 * 
 * 
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 
 * 
 * Note:
 * 
 * All given inputs are in lowercase letters a-z.
 * 
 */
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        int index = 0;
        boolean isPrefix = true;
        String curr = "";
        String model = strs[0].substring(index);
        outerloop:
        while(true) {
            model = strs[0].substring(index);
            for(int i = 1; i < strs.length; i++) {
                if(strs[i].substring(index).length() == 0){
                    break outerloop;
                }
                curr = strs[i].substring(index, index+1);
                if(model != curr) {
                    isPrefix = false;
                    break;
                } 
            }
            if(isPrefix) {
                prefix += model;
            }
            index++;
        }
        
        return prefix;
    }
}

