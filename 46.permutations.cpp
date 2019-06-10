/*
 * @lc app=leetcode id=46 lang=cpp
 *
 * [46] Permutations
 */

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> list;
        vector<int> smallList;
        backtrack(nums, list, smallList);
        return list;
    }
    
    void backtrack(vector<int>& nums, vector<vector<int>>& list, vector<int> smallList) {
        if(nums.size() == 0){
            list.push_back(smallList);
            return;
        } else {
            for(int i = 0; i < nums.size(); i++) {
                cout << nums[i] << endl;
                int temp = nums[i];
                smallList.push_back(nums[i]);
                swap(nums, i, nums.size() - 1);
                nums.erase(nums.begin());
                backtrack(nums, list, smallList);
                smallList.pop_back();
                nums.insert(nums.begin(), temp);
            }
        }
    }

    void swap(vector<int>& nums, int x, int y ){
        int temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
    }
};

