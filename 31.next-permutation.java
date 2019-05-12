/*
 * @lc app=leetcode id=31 lang=java
 *
 * [31] Next Permutation
 *
 * https://leetcode.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (30.27%)
 * Total Accepted:    230.3K
 * Total Submissions: 758.8K
 * Testcase Example:  '[1,2,3]'
 *
 * Implement next permutation, which rearranges numbers into the
 * lexicographically next greater permutation of numbers.
 * 
 * If such arrangement is not possible, it must rearrange it as the lowest
 * possible order (ie, sorted in ascending order).
 * 
 * The replacement must be in-place and use only constant extra memory.
 * 
 * Here are some examples. Inputs are in the left-hand column and its
 * corresponding outputs are in the right-hand column.
 * 
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 * 
 */
class Solution {
    public void nextPermutation(int[] nums) {
        int index = nums.length  - 1;
        while(index - 1 >= 0 && nums[index - 1] >= nums[index]){
            index--;
        }
        if(index - 1 >= 0){
            int greater = 0;
            for(int i = nums.length - 1; i > index - 1; i--) {
                if(nums[i] > nums[index - 1]){
                    greater = i; 
                    break;
                }
            }
            swap(nums, greater, index - 1);
        }
        int a = index, b = nums.length - 1;
            while (a < b) {
                swap(nums, a, b);
                a++;
                b--;
            }
    }
    void swap(int [] nums, int a, int b){
        int temp = nums[b];
        nums[b] = nums[a];
        nums[a] = temp;
    }   
}

