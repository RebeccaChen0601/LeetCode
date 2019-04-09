import java.util.Arrays;

/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms
 * Medium (23.67%)
 * Total Accepted:    514.8K
 * Total Submissions: 2.2M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the
 * sum of zero.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate triplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [-1, 0, 1, 2, -1, -4],
 * 
 * A solution set is:
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 * 
 */

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        if (nums == null || nums.length == 0 || (nums.length < 3)) {
            return list;
        }
        Arrays.sort(nums);
        int i = 0, k = 1, j = nums.length - 1, ans = 0;
        while(i < k && k < j){
            System.out.println("i: " + i + " k: " + k + " j: " + j);
            ans = nums[i] + nums[k] + nums [j];
            if(ans > 0){
                if (k + 1 < j && nums[j - 1] != nums[j]) {
                    j--;
                    while(k + 1 < j && nums[j + 1] == nums[j]) j--; 
                    continue;
                }
            } else if(ans == 0) {
                List<Integer> intList = new ArrayList<>();
                intList.add(nums[i]);
                intList.add(nums[k]);
                intList.add(nums[j]);
                list.add(intList);
            }     
            if(i + 1 == k && k + 1 == j) break;
            if(k + 1 < j){
               k++;
               while (k + 1 < j && nums[k] == nums[k-1]) k++;
            } else if(i + 1 < k) {
                i++;
                k = i+1;
                while(i + 1 < k && nums[i - 1] == nums[i]) {
                    i++;
                    k = i+1;
                }
            } else break;
            continue;
        }
        return list;
    }
}
