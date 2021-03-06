import java.util.ArrayList;

/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 *
 * https://leetcode.com/problems/palindrome-number/description/
 *
 * algorithms
 * Easy (42.54%)
 * Total Accepted:    544.2K
 * Total Submissions: 1.3M
 * Testcase Example:  '121'
 *
 * Determine whether an integer is a palindrome. An integer is a palindrome
 * when it reads the same backward as forward.
 * 
 * Example 1:
 * 
 * 
 * Input: 121
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: -121
 * Output: false
 * Explanation: From left to right, it reads -121. From right to left, it
 * becomes 121-. Therefore it is not a palindrome.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 10
 * Output: false
 * Explanation: Reads 01 from right to left. Therefore it is not a
 * palindrome.
 * 
 * 
 * Follow up:
 * 
 * Coud you solve it without converting the integer to a string?
 * 
 */
class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0 || (x != 0 && x % 10 == 0)) return false;
        if(x < 10) return true;
        int num = 0;
        while(x > num) {
            if(x % 10 == 0) num = num * 10;
            else num = num * 10 + x % 10;
            x /= 10;
        }
        if(num == x || (num / 10 == x && num / 10 != 0)) return true;
        return false;
    }

    public boolean isPalindromeSolution(int x) {
        if(x < 0 || (x != 0 && x % 10 == 0)) return false;
        int num = 0;
        while(x > num) {
            num = num * 10 + x % 10;
            x /= 10;
        }
        return (num == x || (num / 10 == x && num / 10 != 0));
    }
    // optimization: 
    //      1. generalization: classify cases into main categories
    //      2. Special cases: identify (un)neccessary special cases
}

