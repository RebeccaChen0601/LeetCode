/*
 * @lc app=leetcode id=33 lang=java
 *
 * [33] Search in Rotated Sorted Array
 *
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (32.77%)
 * Total Accepted:    401.8K
 * Total Submissions: 1.2M
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 * 
 * (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
 * 
 * You are given a target value to search. If found in the array return its
 * index, otherwise return -1.
 * 
 * You may assume no duplicate exists in the array.
 * 
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 3
 * Output: -1
 * 
 */
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1, mid = 0;
        if(nums.length < 1 || (target < nums[left] && target > nums[right])) return -1;
        int pivot = findPivot(nums, left, right);
        while(left <= right){
            mid = (left + right) / 2;
            if(target == nums[(mid + pivot) % nums.length]){
                return (mid + pivot) % nums.length;
            } else if(target < nums[(mid + pivot) % nums.length]){
                right = mid - 1;
            } else if(target > nums[(mid + pivot) % nums.length]){
                left = mid + 1;
            }
        }
        if(nums.length == 1 && target == nums[mid]) return 0;
        return -1;
    }

    int findPivot(int[] nums, int left, int right){
        int mid = 0;
        while(left < right && nums[left] > nums[right]) {
            mid = (right + left) / 2;
            if(nums[mid] > nums[right]){
                left = mid + 1;
            } else {
                right = mid;
            } 
        }
        return left;
    }
}

