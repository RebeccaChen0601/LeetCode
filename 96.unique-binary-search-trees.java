/*
 * @lc app=leetcode id=96 lang=java
 *
 * [96] Unique Binary Search Trees
 */
class Solution {
    
    // DP Solution: 从局部到整体，从小到大， 从base case入手，让他accumulate。deduction 思想
    // public int numTrees(int n) {
    //     int [] tree = new int[n+1];
    //     tree[1] = tree[0] = 1;
    //     for(int i = 2; i <= n; i++) { // index of the tree, starting from 2
    //         for(int j = 0; j < i; j++){  
    // 从实际操作先入手再想for loop index: 左边tree num + 右边tree num
    // think from base case: if n = 2, we would have an empty left child and 1 right child.
    // then j must start from 0; and since we want the last left tree result to be n - 1 th tree
    // result, j must < i.
    //             tree[i] += (tree[j] * tree[i - 1 - j]);
    //         }
    //     }
    //     return tree[n];
    // }
    
    
    //backTracking: 从整体到局部，由大到小，base case写好，
    //              recursion想象他已经得到结果之后的处理，induction思想
    // public int numTrees(int n) {
    //     if(n == 1 || n == 0) { // empty leaf or single leaf
    //         return 1;
    //     }
    //     int num = 0;
    //     // 0 ~ n - 1 subtrees divided into left and right
    //     for(int i = 0; i < n; i++) {
    //         num += numTrees(i) * numTrees(n - i - 1);
    //     }
    //     return num;
    // }
    
    //backTracking void: 从整体到局部，由大到小，base case先写好，make sure the same node is not recalculated 
    //                   recursion想象他已经得到结果之后的处理，induction思想
    public int numTrees(int n) {
        int [] tree = new int[n+1];
        tree[1] = tree[0] = 1; 
        numTreesHelper(tree, n);
        return tree[n];
    }
    
    void numTreesHelper(int []tree, int n) {
        if(tree[n] != 0) return;  // make sure the same node is not recalculated
        for(int i = 0; i < n; i++) {
            numTreesHelper(tree, i); 
            numTreesHelper(tree, n - i - 1); 
            tree[n] += tree[i] * tree[n - i - 1];
        }
    }
}
    
   
