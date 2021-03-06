import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode id=17 lang=java
 *
 * [17] Letter Combinations of a Phone Number
 *
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (41.04%)
 * Total Accepted:    371.4K
 * Total Submissions: 904.2K
 * Testcase Example:  '"23"'
 *
 * Given a string containing digits from 2-9 inclusive, return all possible
 * letter combinations that the number could represent.
 * 
 * A mapping of digit to letters (just like on the telephone buttons) is given
 * below. Note that 1 does not map to any letters.
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Input: "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * 
 * 
 * Note:
 * 
 * Although the above answer is in lexicographical order, your answer could be
 * in any order you want.
 * 
 */
class Solution {
    Map<String, String> map = new HashMap<String, String>() {{
        put("2", "abc");
        put("3", "def");
        put("4", "ghi");
        put("5", "jkl");
        put("6", "mno");
        put("7", "pqrs");
        put("8", "tuv");
        put("9", "wxyz");
      }};
    
    List<String> output = new ArrayList<String>();

    public List<String> letterCombinations(String digits) {
        if(digits.length() != 0) backTrack("", digits);
        return output;
    }

    void backTrack(String combination, String next_digits){
        if(next_digits.length() == 0) output.add(combination);
        else {
            String letters = map.get(next_digits.substring(0, 1));
            for(int i = 0; i < letters.length(); i++){
                backTrack(combination + map.get(next_digits.substring(0, 1)).substring(i, i+1), next_digits.substring(1));
            }
        }  
    }
    //思路：for loop + recursion：多条路线发展 
}

