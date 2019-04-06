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
        int number = 0, index = 0;
        ArrayList<Integer> num = new ArrayList<Integer>();
        boolean isNeg = (x < 0) ? true : false;
        x = isNeg ? -x : x;
        while(x >= 0) {
            num.add(x % 10);
            x = x / 10; 
            index++;
        }
        for(int i = 0; i < index; i++) {
            number += num.get(i) * (int)Math.pow(10, index - i - 1);
        }
        number = isNeg ? -number : number;
        return number;
    }
}



