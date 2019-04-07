import java.util.ArrayList;

/*
 * @lc app=leetcode id=7 lang=java
 *
 * [7] Reverse Integer
 *
 * https://leetcode.com/problems/reverse-integer/description/
 *
 * algorithms
 * Easy (25.23%)
 * Total Accepted:    649.3K
 * Total Submissions: 2.6M
 * Testcase Example:  '123'
 *
 * Given a 32-bit signed integer, reverse digits of an integer.
 * 
 * Example 1:
 * 
 * 
 * Input: 123
 * Output: 321
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: -123
 * Output: -321
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 120
 * Output: 21
 * 
 * 
 * Note:
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
 * of this problem, assume that your function returns 0 when the reversed
 * integer overflows.
 * 
 */
class Solution {
    public int reverse(int x) {
        int number = 0, inc = 0;
        while(x != 0) {
            inc = x % 10;
            if (((Integer.MAX_VALUE / 10 < number || (Integer.MAX_VALUE / 10 == number && inc > 7)) && x > 0) || ((Integer.MIN_VALUE / 10 > number || (Integer.MAX_VALUE / 10 == number &&  inc < -8)) && x < 0 )) {
                return 0;
            }
            number = number * 10 + inc;
            x = x / 10;
        }
        return number;
    }
}




