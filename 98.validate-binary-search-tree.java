import java.util.Stack;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=98 lang=java
 *
 * [98] Validate Binary Search Tree
 *
 * https://leetcode.com/problems/validate-binary-search-tree/description/
 *
 * algorithms
 * Medium (25.44%)
 * Total Accepted:    383.4K
 * Total Submissions: 1.5M
 * Testcase Example:  '[2,1,3]'
 *
 * Given a binary tree, determine if it is a valid binary search tree (BST).
 * 
 * Assume a BST is defined as follows:
 * 
 * 
 * The left subtree of a node contains only nodes with keys less than the
 * node's key.
 * The right subtree of a node contains only nodes with keys greater than the
 * node's key.
 * Both the left and right subtrees must also be binary search trees.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input:
 * ⁠   2
 * ⁠  / \
 * ⁠ 1   3
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * ⁠   5
 * ⁠  / \
 * ⁠ 1   4
 * / \
 * 3   6
 * Output: false
 * Explanation: The input is: [5,1,4,null,null,3,6]. The root node's
 * value
 * is 5 but its right child's value is 4.
 * 
 * 
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
        // public boolean isValidBSTCurrentTreeOnly(TreeNode root) {
        //     if(root == null) return true;
        //     if(root.left != null && root.left.val >= root.val || root.right != null && root.right.val <= root.val) {
        //         return false;
        //     } 
        //     return isValidBST(root.left) && isValidBST(root.right);
        //     // 如果只管当前tree的order是正确的，如果全部order都要follow的话就不对了
        // }

        public boolean isValidBST(TreeNode root) {
            Stack<TreeNode> nodes = new Stack();
            double inOrder = Double.MIN_VALUE;
            while(!nodes.isEmpty() || root != null){
                while(root != null){
                    nodes.push(root);
                    root = root.left;
                }
                root = nodes.pop();
                if(root.val <= inOrder) return false; //第一次一定会大于double min，之后都是以左上右顺序比较
                inOrder = root.val;
                root = root.right;
                // root.right如果是null，循环继续但是不进入小循环，直接pop出来的其实是上层node，帮助实现左上右顺序
                //           如果不是，大小循环进入，到右边node的最左，然后此时的inorder比较则是又右边的最左和循环前的上层比较，实现右边永远比左边小
            }
        }

        public int kthSmallest(TreeNode root, int k) {
            Stack<TreeNode> nodes = new Stack();
            while( !nodes.isEmpty() || root != null) {
                while(root != null){
                    nodes.push(root);
                    root = root.left;
                }
                root = nodes.pop();
                k--;
                if(k == 0) break;
                root = root.right;
            }
            return root.val;
        }

        public int sumOfLeftLeaves(TreeNode root) {
            int res = 0;
            if (root == null) return res;
            Stack<TreeNode> stack = new Stack<>();        
            while (root != null || !stack.isEmpty()) {
                while (root != null) {
                    stack.push(root);
                    root = root.right;
                }
                root = stack.pop();
                root = root.left;
                if (root != null && root.left == null && root.right == null) res += root.val;
            }
            return res;
        }

        // a concise solution, start with isValidBSTConsise(root, null, null)
        
        bool isValidBSTConsise(TreeNode root, TreeNode min, TreeNode max) {
            if (root == null) return true;
            if (min != null && root.val <= min.val) return false;
            if (max != null && root.val >= max.val) return false;
            return isValidBST(root.left, min, root) && isValidBST(root.right, root, max);
        }

      

}

