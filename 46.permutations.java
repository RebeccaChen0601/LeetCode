import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=46 lang=java
 *
 * [46] Permutations
 */
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> list = new List<List<Integer>>();
        backTrack(nums, list, new ArrayList<Integer>());
    }

    void backTrack(int[] nums, List<List<Integer>> list, List<Integer> smallList) {
        if(smallList.length == nums.length){
            list.add(new ArrayList(smallList));
            return;
        } else {
            for(int i = 0; i < nums.length; i++){ 
                smallList.add(nums[i]);
                nums.remove(i);
                backTrack(nums, list, smallList);
                nums.add(i);
            }
        }
    }
}

