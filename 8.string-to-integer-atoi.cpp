/*
 * @lc app=leetcode id=8 lang=cpp
 *
 * [8] String to Integer (atoi)
 *
 * https://leetcode.com/problems/string-to-integer-atoi/description/
 *
 * algorithms
 * Medium (14.57%)
 * Total Accepted:    351.6K
 * Total Submissions: 2.4M
 * Testcase Example:  '"42"'
 *
 * Implement atoi which converts a string to an integer.
 * 
 * The function first discards as many whitespace characters as necessary until
 * the first non-whitespace character is found. Then, starting from this
 * character, takes an optional initial plus or minus sign followed by as many
 * numerical digits as possible, and interprets them as a numerical value.
 * 
 * The string can contain additional characters after those that form the
 * integral number, which are ignored and have no effect on the behavior of
 * this function.
 * 
 * If the first sequence of non-whitespace characters in str is not a valid
 * integral number, or if no such sequence exists because either str is empty
 * or it contains only whitespace characters, no conversion is performed.
 * 
 * If no valid conversion could be performed, a zero value is returned.
 * 
 * Note:
 * 
 * 
 * Only the space character ' ' is considered as whitespace character.
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical
 * value is out of the range of representable values, INT_MAX (2^31 − 1) or
 * INT_MIN (−2^31) is returned.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "42"
 * Output: 42
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "   -42"
 * Output: -42
 * Explanation: The first non-whitespace character is '-', which is the minus
 * sign.
 * Then take as many numerical digits as possible, which gets 42.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "4193 with words"
 * Output: 4193
 * Explanation: Conversion stops at digit '3' as the next character is not a
 * numerical digit.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "words and 987"
 * Output: 0
 * Explanation: The first non-whitespace character is 'w', which is not a
 * numerical 
 * digit or a +/- sign. Therefore no valid conversion could be performed.
 * 
 * Example 5:
 * 
 * 
 * Input: "-91283472332"
 * Output: -2147483648
 * Explanation: The number "-91283472332" is out of the range of a 32-bit
 * signed integer.
 * Thefore INT_MIN (−2^31) is returned.
 * 
 */
class Solution {
    public int myAtoi(String str) {
        int res = 0;
        boolean isNeg = false;
        if(str.length() < 1) return 0; 
        while(str.length() > 0 && str.charAt(0) == ' '){
            str = str.substring(1);
        }
        if(str.length() > 0){
            if(str.charAt(0) == '-'){
                isNeg = true;
                str = str.substring(1); 
            } else if(str.charAt(0) == '+'){
                str = str.substring(1);
            } else if(str.charAt(0) < '0' || str.charAt(0) > '9') {
                return 0;
            } 
        } else return 0;
        
        while(str.length() > 0 && str.charAt(0) >= '0' && str.charAt(0) <= '9'){
            if(isNeg && (res > Integer.MIN_VALUE / 10 ||
               (res == Integer.MIN_VALUE / 10 && str.charAt(0) < '9'))){
                res = res * 10 - (str.charAt(0) - '0');
            } else if(isNeg){
                return Integer.MIN_VALUE;
            } else if(res < Integer.MAX_VALUE / 10 || 
                      (res == Integer.MAX_VALUE / 10 && str.charAt(0) < '8')){
                res = res * 10 + str.charAt(0) - '0';
            } else {
                System.out.println(res);
                return Integer.MAX_VALUE;
            }
            str = str.substring(1);
        }
        return res;
    }
    
    public int myAtoiStandard(String str) {
    if (str.trim().isEmpty()) return 0;    
    str = str.trim();
    int sign = 1, base = 0, i = 0;
   
    if (str.charAt(i) == '-' || str.charAt(i) == '+')
        sign = str.charAt(i++) == '-' ? -1 : 1;
    
    while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
        // -21 47 48 36 48 to 21 47 48 36 47
        if (base > Integer.MAX_VALUE / 10 || (base == Integer.MAX_VALUE / 10 && str.charAt(i) - '0' > 7)) {
            return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
        }
        base = 10 * base + (str.charAt(i++) - '0');
    }
    return base * sign;
}
}
