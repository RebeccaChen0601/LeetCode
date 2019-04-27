/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (36.23%)
 * Total Accepted:    567.7K
 * Total Submissions: 1.6M
 * Testcase Example:  '"()"'
 *
 * Given a string containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * 
 * 
 * Note that an empty string is also considered valid.
 * 
 * Example 1:
 * 
 * 
 * Input: "()"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "()[]{}"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "(]"
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "([)]"
 * Output: false
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: "{[]}"
 * Output: true
 * 
 * 
 */
class Solution {
    public boolean isValid(String s) { 
        Map<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        Stack<Character> stack = new Stack<Character>(); 
        
        for(int i = 0; i < s.length(); i++){
            // System.out.println(s.charAt(i));
            if(map.containsKey(s.charAt(i))){
                // System.out.println(map.containsKey(s.charAt(i))+ "lala");
                stack.push(s.charAt(i));
                // System.out.println(map.get(stack.peek()) + "" + s.charAt(i+1)+stack.empty());
            } else if(stack.empty() || 
                      (!stack.empty() && s.charAt(i) != map.get(stack.pop()))){
                System.out.println(stack.empty());
                return false;
            }
            
        }
        if(stack.empty())
        return true;
        return false;
    }
}

