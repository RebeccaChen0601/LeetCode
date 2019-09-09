/*
 * @lc app=leetcode id=75 lang=java
 *
 * [75] Sort Colors
 */
class Solution {
    public void sortColors(int[] nums) {
        int index0 = -1, index2 = nums.length;
        int i = 0;
        while(index0 + 1 < nums.length && index2 - 1 >= 0 && i > -1 && i < nums.length) {
            if(nums[i] == 2 && i != index2 - 1) {
                if(nums[index2 - 1] == 0) {
                    swap(i, index2 - 1, nums);
                    index0++;
                    i = index2 - 1; 
                } else if(nums[index2 - 1] == 1){
                    swap(i, index2 - 1, nums);
                    i = index2 - 1; 
                } else{
                    while(index2 > 0 && nums[index2 - 1] == 2) {
                        index2--;
                    }
                }
            } else if (nums[i] == 0 && i != index0 + 1) {
                if(nums[index0 + 1] == 0) {
                    while(index0 > nums.length && nums[index0 + 1] == 0) {
                        index0++;
                    }
                }else if(nums[index0 + 1] == 1) {
                    swap(i, index0+1, nums);
                    i = index0 + 1;
                }else if(nums[index0 + 1] == 2) {
                    swap(i, index0+1, nums);
                    i = index0 + 1;
                    index2--;
                }
            } else {
                if() i++;
                else i--; 
            } 
        }  
    }

    void swap(int i, int j, int[] nums) {
        int temp = nums[i]; 
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

