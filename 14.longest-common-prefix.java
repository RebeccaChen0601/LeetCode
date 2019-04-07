import java.util.HashMap;

/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (33.19%)
 * Total Accepted:    435.4K
 * Total Submissions: 1.3M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 * Example 1:
 * 
 * 
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 
 * 
 * Note:
 * 
 * All given inputs are in lowercase letters a-z.
 * 
 */
class Solution {
    public String longestCommonPrefix(String[] strs) {
        Trie trie = new Trie(new Node(0));
        int index = 0;
        for(int i = 0; i < strs.length; i++) {
            trie.insertWord(strs[i], ++index);
        }
        return trie.findPrefix();
    }
   
}
class Trie {
    Node node;
    Trie(Node node){
        this.node = node;
    }
    void insertWord(String word, int index) {
        char [] chars = word.toCharArray();
        for(int i = 0; i < chars.length; i++) {
            if(node.index == index - 1){
                node.map.put(chars[i], new Node(index));
            } else {
                node.map.put(chars[i], null);
            }
        }
    }

    String findPrefix(){
        String prefix = "";
        while(node) {
            prefix += node.map.keySet().toArray()[0];
            node = node.map.get(node.map.keySet().toArray()[0]);
        }
        return prefix;
    }
} 

class Node {
    HashMap<Character, Node> map = new HashMap<Character, Node>();
    int index;
    Node(int index){
        this.index = index;
    }
}

