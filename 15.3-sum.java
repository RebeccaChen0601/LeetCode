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
        Arrays.sort(nums);
        List<List<Integer>> list = new LinkedList<>();
        for(int i = 0; i < nums.length - 2; i++) {
            if(i==0 || nums[i] != nums[i - 1]){
                int lo = i+1,hi=nums.length-1, sum = 0 - nums[i];
                while(lo < hi){
                    if(nums[lo] + nums[hi] == sum){
                        list.add(Arrays.asList(nums[i], nums[lo], nums[hi]));
                        while(lo < hi && nums[lo] == nums[lo+1]) lo++;
                        while(lo < hi && nums[hi] == nums[hi-1]) hi--;
                        lo++; hi--;
                    } else if(nums[lo] + nums[hi] < sum) lo++;
                    else hi--;
                }
            }
        }
        return list;
    }

    // 思路差距： 
    // 1. 三个variabels思路，先固定一个变换另两个； 我的思路三个同时在变
    // 2. 当找到0的时候同时两个值lo,hi变大变小才有可能拼凑出下一个结果
    // 3. 明确的结束condition
    // 4. tranverse思路从左到右比在中间结束好处理
    
    public List<List<Integer>> threeSumFail(int[] nums) {
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
                j--;
            } else if(ans == 0) {
                List<Integer> intList = new ArrayList<>();
                intList.add(nums[i]);
                intList.add(nums[k]);
                intList.add(nums[j]);
                list.add(intList);
                while (k < j && nums[k] == nums[k+1]) k++;
                while( j > k && nums[j - 1] == nums[j]) j--; 
                k++;
                j--;
            } else if(k+1 == j){
                i++;
                k=i+1;
            }

            if(i + 1 == k && k + 1 == j) break;
        }
        return list;
    }
}

