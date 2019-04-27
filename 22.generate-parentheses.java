/*
 * @lc app=leetcode id=22 lang=java
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (54.10%)
 * Total Accepted:    325.8K
 * Total Submissions: 599.6K
 * Testcase Example:  '3'
 *
 * 
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 * 
 * 
 * 
 * For example, given n = 3, a solution set is:
 * 
 * 
 * [
 * ⁠ "((()))",
 * ⁠ "(()())",
 * ⁠ "(())()",
 * ⁠ "()(())",
 * ⁠ "()()()"
 * ]
 * 
 */
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList();
        backTrack(ans, "", 0, 0, n);
        return ans;
    }
    
    public void backTrack(List<String> ans, String cur, int front, int back, int max){
        if(cur.length() == max * 2) {
            ans.add(cur);
            return;
        }
        if(front < max){
            backTrack(ans, cur+"(", front+1, back, max);
        } 
        if(front > back) {
            backTrack(ans, cur+")", front, back+1, max);
        } 
        
    }
}

