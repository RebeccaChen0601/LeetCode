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
        Trie trie = new Trie();
        int index = 0;
        for(int i = 0; i < strs.length; i++) {
            trie.insertWord(strs[i], ++index);
        }
        return trie.findPrefix();
    }
   
}
class Trie {
    Node node;
    Trie(){
        node = new Node(0);
    }
    void insertWord(String word, int index) {
        Node curr = node;
        for(char c : word.toCharArray()){
            if (curr.index == index - 1){
                curr.map.putIfAbsent(c, new Node(index));
            } else {
                curr.map.put(c, null);
            }
            curr = curr.map.get(c);
        }
    }

    String findPrefix(){
        String prefix = "";
        while(this.node != null) {
            prefix += this.node.map.keySet().toArray()[0];
            node = this.node.map.get(this.node.map.keySet().toArray()[0]);
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

